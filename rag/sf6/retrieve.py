class Retrive:
  """
  Retrievers

  Once the data is in the database, you still need to retrieve it.
  LangChain supports many different retrieval algorithms and is one of the places where we add the most value.
  We support basic methods that are easy to get started - namely simple semantic search.
  However, we have also added a collection of algorithms on top of this to increase performance. These include:

  - Parent Document Retriever: This allows you to create multiple embeddings per parent document, allowing you to look up smaller chunks but return larger context.
  - Self Query Retriever: User questions often contain reference to something that isn't just semantic, but rather expresses some logic that can best be represented as a metadata filter. Self-query allows you to parse out the semantic part of a query from other metadata filters present in the query
  - Ensemble Retriever: Sometimes you may want to retrieve documents from multiple different sources, or using multiple different algorithms. The ensemble retriever allows you to easily do this.
  - And more!
  """
  
  def __init__(self) -> None:
    pass
  
  def execute(self) -> None:
    pass