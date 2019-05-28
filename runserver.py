# from app import APIServer
# if __name__ == '__main__':
#     server = APIServer('prod').run()

from app import APIServer
if __name__ == '__main__':
    app = APIServer('prod')
    app.run()
else:
    app = APIServer('prod')
    app.run()

