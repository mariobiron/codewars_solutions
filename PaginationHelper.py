# For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class,
# which is a utility class helpful for querying paging information related to an array.
# The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page.
# The types of values contained within the collection/array are not relevant.
# The following are some examples of how this class is used:
# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.my_col = list(collection)
        self.pages = []
        for x in range(0,(len(collection)//items_per_page)+1):
            self.pages.append(self.my_col[x*items_per_page:(x*items_per_page)+items_per_page])
        self.ipp = items_per_page
        return None

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.my_col)

    # returns the number of pages
    def page_count(self):
        import math
        return math.ceil((len(self.my_col)/self.ipp))

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self ,page_index):
        retval = -1
        if page_index < len(self.pages) and page_index >= 0:
            retval = len(self.pages[page_index])
        return retval

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self ,item_index):
        retval = -1
        if item_index < len(self.my_col) and item_index >= 0:
            retval = item_index//self.ipp
        return retval


helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
print('Page count = '+str(helper.page_count())) # should == 2
print('Item count = '+str(helper.item_count())) # should == 6
print('Page 0 Item count = '+str(helper.page_item_count(0)))  # should == 4
print('Page 1 Item count = '+str(helper.page_item_count(1))) # last page - should == 2
print('Page 2 Item count = '+str(helper.page_item_count(2))) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
print('Page Index for item 5 = '+str(helper.page_index(5))) # should == 1 (zero based index)
print('Page Index for item 2 = '+str(helper.page_index(2))) # should == 0
print('Page Index for item 20 = '+str(helper.page_index(20))) # should == -1
print('Page Index for item -10 = '+str(helper.page_index(-10))) # should == -1 because negative indexes are invalid

collection = range(1,25)
helper2 = PaginationHelper(collection, 10)

print('Page Count = '+str(helper2.page_count())) #, 3, 'page_count is returning incorrect value.')
print('Page Index for item 23 = '+str(helper2.page_index(23))) #, 2, 'page_index returned incorrect value')
print('Item Count = '+str(helper2.item_count())) #, 24, 'item_count returned incorrect value')