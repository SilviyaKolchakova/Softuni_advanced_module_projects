class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents =[]

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def get_obj_by_id(obj_id, collection):
        for el in collection:
            if el.id == obj_id:
                return el

    def edit_category(self, category_id, new_name):
        category = self.get_obj_by_id(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.get_obj_by_id(topic_id, self.topics)

        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.get_obj_by_id(document_id, self.documents)

        document.file_name = new_file_name

    def delete_obj(self,obj_id, collection):
        obj = self.get_obj_by_id(obj_id, collection)
        collection.remove(obj)

    def delete_category(self, category_id):
        self.delete_obj(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.delete_obj(topic_id, self.topics)

    def delete_document(self, document_id):
        self.delete_obj(document_id, self.documents)

    def get_document(self, document_id):
        return self.get_obj_by_id(document_id, self.documents)

    def __repr__(self):
        result = ''

        result += ''.join([document.__repr__() for document in self.documents])
        return result
