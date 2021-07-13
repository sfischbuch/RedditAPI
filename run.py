import redditpraw as rp

# data = rp.process_data("ENFJ")
# # data = rp.process_data("ENFJ")
# data.head(10)

# Run later
for type in rp.MTBTI_TYPES:
    rp.process_data(type, "{}_data_set".format(type))

