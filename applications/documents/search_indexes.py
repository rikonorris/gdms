from haystack import indexes
from documents.models.base import DocumentMeta


class ContractIndex(indexes.SearchIndex, indexes.Indexable):
     text = indexes.CharField(document=True, use_template=True)

     title = indexes.CharField(model_attr='title')
     order_num = indexes.CharField(model_attr='order_num')
     type = indexes.CharField(model_attr='type')
     status = indexes.CharField(model_attr='status')
     date_created = indexes.CharField(model_attr='date_created')

     def get_model(self):
         return DocumentMeta

     def index_queryset(self, using=None):
         return self.get_model().objects.all()
