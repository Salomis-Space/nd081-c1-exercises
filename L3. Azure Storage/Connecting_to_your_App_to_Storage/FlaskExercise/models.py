'''from FlaskExercise import app, db
from flask import flash
from werkzeug.utils import secure_filename
from azure.storage.blob import BlobServiceClient
import uuid

blob_container = app.config['BLOB_CONTAINER']
storage_url = "https://{}.blob.core.windows.net/".format(app.config['BLOB_ACCOUNT'])
blob_service = BlobServiceClient(account_url=storage_url, credential=app.config['BLOB_STORAGE_KEY'])

class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75))
    scientific_name = db.Column(db.String(75))
    description = db.Column(db.String(800))
    image_path = db.Column(db.String(100))

    def __repr__(self):
        return '<Animal {}>'.format(self.body)

    def save_changes(self, file):
        if file:
            filename = secure_filename(file.filename)
            fileExtension = filename.rsplit('.', 1)[1]
            randomFilename = str(uuid.uuid1())
            filename = randomFilename + '.' + fileExtension
            try:
                # TODO: Get a blob client and upload the blob
                pass
                if self.image_path:
                    # TODO: Get a blob client and delete the previous blob
                    pass
            except Exception as err:
                flash(err)
            self.image_path = filename
        db.session.commit()
'''

from FlaskExercise import app, db
from flask import flash
from werkzeug.utils import secure_filename
from azure.storage.blob import BlobServiceClient
import uuid

# ---------- Blob setup ----------
blob_container = app.config['BLOB_CONTAINER']
blob_service = BlobServiceClient(
    account_url=f"https://{app.config['BLOB_ACCOUNT']}.blob.core.windows.net",
    credential=app.config['BLOB_STORAGE_KEY']
)

class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75))
    scientific_name = db.Column(db.String(75))
    description = db.Column(db.String(800))
    image_path = db.Column(db.String(100))

    def __repr__(self):
        return '<Animal {}>'.format(self.name)

    def save_changes(self, file):
        """
        Save changes to the database and upload the file to Blob Storage if provided.
        """
        if file:
            # Generate a secure, unique filename
            filename = secure_filename(file.filename)
            file_extension = filename.rsplit('.', 1)[1]
            random_filename = str(uuid.uuid1())
            filename = random_filename + '.' + file_extension

            try:
                # Upload new image to Blob Storage
                blob_client = blob_service.get_blob_client(container=blob_container, blob=filename)
                blob_client.upload_blob(file, overwrite=True)

                # Delete old image from Blob Storage if exists
                if self.image_path:
                    old_blob = blob_service.get_blob_client(container=blob_container, blob=self.image_path)
                    old_blob.delete_blob()
            except Exception as err:
                flash(err)

            self.image_path = filename

        db.session.commit()
