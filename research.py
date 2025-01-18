import pickle
x = [[1, 2, 3, 4], [5, 6, 7, 8]]

# Save as a pickle file
with open('x.pkl', 'wb') as f:
    pickle.dump(x, f)


with open('x.pkl', 'rb') as f:
    loaded_x = pickle.load(f)

print(loaded_x[0][0])