import numpy as np
import tensorflow as tf
from keras_facenet import FaceNet
import PIL
import pickle


# model = FaceNet().model

# def img_to_encoding(image_path, model):
#     img = tf.keras.preprocessing.image.load_img(image_path, target_size=(160, 160))
#     img = np.around(np.array(img) / 255.0, decimals=12)
#     x_train = np.expand_dims(img, axis=0)
#     embedding = model.predict_on_batch(x_train)
#     return embedding / np.linalg.norm(embedding, ord=2)

# def verify(image_path, identity, database, model):
#     """
#     Function that verifies if the person on the "image_path" image is "identity".
    
#     Arguments:
#         image_path -- path to an image
#         identity -- string, name of the person you'd like to verify the identity. Has to be an employee who works in the office.
#         database -- python dictionary mapping names of allowed people's names (strings) to their encodings (vectors).
#         model -- your Inception model instance in Keras
    
#     Returns:
#         dist -- distance between the image_path and the image of "identity" in the database.
#         door_open -- True, if the door should open. False otherwise.
#     """
#     ### START CODE HERE
#     # Step 1: Compute the encoding for the image. Use img_to_encoding() see example above. (≈ 1 line)
#     encoding = img_to_encoding(image_path, model)
#     # Step 2: Compute distance with identity's image (≈ 1 line)
#     dist = np.linalg.norm(encoding - database[identity], ord=2)
#     # Step 3: Open the door if dist < 0.7, else don't open (≈ 3 lines)
#     if dist < 0.7:
#         print("It's " + str(identity) + ", welcome in!")
#         door_open = True
#     else:
#         print("It's not " + str(identity) + ", please go away")
#         door_open = False
#     ### END CODE HERE        
#     return dist, door_open

# database = {}
# database["danielle"] = img_to_encoding("images/danielle.png", model)
# print(database["danielle"][0])
# database["younes"] = img_to_encoding("images/younes.jpg", model)
# database["tian"] = img_to_encoding("images/tian.jpg", model)
# database["andrew"] = img_to_encoding("images/andrew.jpg", model)
# database["kian"] = img_to_encoding("images/kian.jpg", model)
# database["dan"] = img_to_encoding("images/dan.jpg", model)
# database["sebastiano"] = img_to_encoding("images/sebastiano.jpg", model)
# database["bertrand"] = img_to_encoding("images/bertrand.jpg", model)
# database["kevin"] = img_to_encoding("images/kevin.jpg", model)
# database["felix"] = img_to_encoding("images/felix.jpg", model)
# database["benoit"] = img_to_encoding("images/benoit.jpg", model)
# database["arnaud"] = img_to_encoding("images/arnaud.jpg", model)
# database["hoan"] = img_to_encoding("images/hoan.png", model)


# # Lưu database vào tệp data.pickle
# with open('data.pickle', 'wb') as handle:
#     pickle.dump(database, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Đọc database từ tệp data.pickle
with open('data.pickle', 'rb') as handle:
    loaded_database = pickle.load(handle)

# Kiểm tra xem việc tải lại đã thành công hay không
print(loaded_database["hoan"])