class MongoConnection:
    _instance = None
    count = 0
    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(MongoConnection, cls).__new__(cls)
            cls._instance.__initialized = False
            # Put any initialization here.
        cls.count +=1
        return cls._instance
    
    def __init__(self, host, port):
        if not self.__initialized:
            print('Initializing the object with host: {} and port: {}'.format(host, port))
            # Put any initialization code here.
            self.host = host
            self.port = port
            self.__initialized = True