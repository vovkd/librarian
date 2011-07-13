#!/bin/env python
# Define a book object

class book:
  ''' Define book properties here '''
  def __init__(self):
    self.id = ''
    self.isbn = ''
    self.authors = ''
    self.title = ''
    self.publisher = ''
    self.abstract = ''
    self.mtype = ''
    self.year = ''
    self.city = ''
    self.copies = 0
    self.where = 0

  def print_book(self):
    ## Return some book details as a string for printing.  Mostly a debug thing.
    bookstring = self.isbn + "\n" + self.authors + "\n" + self.title
    return bookstring

  def add_details(self,details_list):
    ''' A simple interface to add all details in one go.  Obviously order
    of the elements is important! id and copies are determined by the
    database after insertion.  The order is:
    isbn, authors, title, abstract, mtype, publisher, year, city
    Empty fields are allowed.
    '''
    try:
      self.isbn = details_list[0]
      self.authors = details_list[1]
      self.title = details_list[2]
      self.publisher = details_list[5]
      self.abstract = details_list[4]
      self.mtype = details_list[3]
      self.year = details_list[6]
      self.city = details_list[7]
      self.copies = details_list[8]
      self.where = details_list[9]
    except: return -1

  def compare(self, book):
    ''' Determine if two books differ.  Return 0 if same and number of
    differences if different. '''
    error = 0
    error += (self.isbn != book.isbn)
    error += (self.authors != book.authors)
    error += (self.title != book.title)
    error += (self.publisher != book.publisher)
    error += (self.abstract != book.abstract)
    error += (self.mtype != book.mtype)
    #error += (self.year != book.year)
    error += (self.city != book.city)
    error += (self.mtype != book.mtype)
    return error


  def webquery(self,isbn):
    import book
    from biblio.webquery.xisbn import XisbnQuery
    import biblio.webquery
    a = XisbnQuery()
    try:
      abook = a.query_bibdata_by_isbn(isbn)
      nn = abook.pop()
      self.id=nn.id
      self.isbn=nn.id
      self.title=nn.title
      self.authors=(str(nn.authors)).replace('[','').replace(']','')
      self.abstract=(nn.abstract)
      self.mtype=nn.type
      self.publisher=(nn.publisher)
      self.city=(nn.city)
      self.year=(nn.year)
    except:
      return 1

# Test harness
if __name__ == "__main__":
  abook = book()
  #abook.webquery("0752272225")
  #abook.webquery("075227222")
  #abook.print_book()

