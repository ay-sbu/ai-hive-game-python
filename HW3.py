
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds


data_set = pd.read_csv("twitch.csv")

user_id = list(map(int, data_set["user_id"].tolist()))


streamer_name = list(map(int,data_set["streamer_name"].tolist()))
channel_score = list(map(float ,data_set["channel_score"].tolist()))

matrix = csr_matrix((channel_score,(user_id,streamer_name)))

print(matrix.shape)
U, S, VT = svds(matrix, k=75)

print(U.shape)
print(S.shape)
print(VT.shape)

# print(matrix.dtype)
# print(matrix.shape)