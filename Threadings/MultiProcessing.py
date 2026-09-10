# import multiprocessing
# import requests

# def downloadfile(url, name):
#     response= requests.get(url)

#     open(f"files/file{name}.jpg","wb").write(response.content)

# if __name__ == "__main__":
            
#             url="http://picsum.photos/2000/3000"
#             pros=[]

#             for i in range(5):
#             # downloadfile(url, i)
#                 p=multiprocessing.Process(target=downloadfile, args=[url,i])

#                 p.start()
#                 pros.append(p)

#             for p in pros:
#                 p.join()





import multiprocessing
import requests

def downloadfile(url, name):
    response = requests.get(url)
    with open(f"files/file{name}.jpg", "wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    url = "http://picsum.photos/2000/3000"
    pros = []

    for i in range(5):
        p = multiprocessing.Process(target=downloadfile, args=(url, i))
        p.start()
        pros.append(p)

    # join AFTER starting all processes
    for p in pros:
        p.join()