from time import sleep;
from os import system;

ids = [];
books = [];
authors = [];
available_status = [];
running = True;

def add_book(l_id, title, author, available_n):
	if not l_id and not title and not authors and not available_n:
		return("Some information has missing, Please try again !");
	elif l_id in ids and Title in books:
		return("The book has existed in system !");
	else:
		ids.append(l_id);
		books.append(title);
		authors.append(author);
		available_status.append(available_n);
		return(f'The book {title} has been added with ID {l_id}');

def search_book(l_id): #enter ID
	if not ids:
		return('There are do not have any book in system to search !');
	else:
		i = ids.index(l_id);
		return(f'ID: {l_id}\nTittle: {books[i]}\nAuthor: {authors[i]}\nAvailable Status: {available_status[i]}');
		#because this function will search only one book so use return to response result immediately

def edit_book(l_id): #enter ID
	query = ids.index(l_id);
	if l_id not in ids:
		return(f'ID {n_id} not found !');
		sleep(2);
	else:
		input(f'Do you want edit Book {books[query]} with ID {ids[query]} ?\nPress Enter to edit');
		
		n_title = input("Enter new title: ");
		n_author = input("Enter new author: ");
		n_status = input("Enter new available status [Avaiable, Not Avaiable]: ");
		
		books[query] = n_title;
		authors[query] = n_author;
		available_status[query] = n_status;

		return(f'Has been edited Book ID {l_id} to: \nTitle: {n_title}\nAuthor:{n_author}\nStatus: {n_status}');

def delete_book(l_id): # Enter ID of book to delete

	if l_id not in ids:
		return(f'The ID {l_id} not in system !');
	else:
		query = ids.index(l_id);
		sto_book = f'The book {books[query]} with ID {ids[query]} Author: {authors[query]} has been deleted'
		del ids[query];
		del books[query];
		del authors[query];
		del available_status[query];
		return(sto_book);

def show_all():
	if not ids:
		return('There are do not have any book in system !');
	else:
		for i in range(len(ids)):
			print(f'ID: {ids[i]}\nTitle: {books[i]}\nAuthor: {authors[i]}\nStatus: {available_status[i]}\n\n');
	sleep(2);

def borrow(l_id):
	query = ids.index(l_id);
	if l_id not in ids:
		return(f'there are do not have book with ID {l_id} to borrow !');
	else:
		if available_status[query] == 'unavailable':
			return('The book is unavailable to borrow. Please try later');
		else:
			available_status[query] = 'unavailable';
			return(f"The books {books[query]}, Author {authors[query]} has been borrowed. \
				Status will change from available to {available_status[query]}");

def return_book(l_id):
	if l_id not in ids:
		return(f'ID {l_id} not in system !');
	else:
		query = ids.index(l_id);
		if available_status[query] == 'available':
			return(f'the book {books[query]} has exist in System. You cannot return this book');
		else:
			available_status[query] = 'available';
			return(f'The book {books[query]} has been returned to system. Status will be change from unavailable to {available_status[query]}'); 

if __name__ == "__main__":
	while running:
		system('cls')
		print(f"Welcome to Book Management System\n\nPlease Select Number To Run Function\
			\n1. Add New Book\n2. Search Book\n3. Edit Book\n4. Delete Book\n5. Show All Book\
			\n6. Borrow A Book\n7. Return A Book\n8. Quit Program");
		choose = int(input("Choose Your Option: "));

		if (choose <= 0) and (choose > 8):
			print("Wrong Option ");
			sleep(2);
		elif choose == 1:
			# add book
			print(add_book(int(input('Enter new ID: ')), input('Enter new title of book: '), \
				input('Enter author name: '), input('Enter status\n[available, unavailable]: ').lower())); sleep(2);
		elif choose == 2:
			# search book
			print(search_book(int(input('Enter book ID to searh: '))));
			sleep(2);
		elif choose == 3:
			# edit book
			print(edit_book(int(input("Enter ID of book to edit: "))));
			sleep(2)
		elif choose == 4:
			# delete book
			print(delete_book(int(input('Enter ID of book to delete: '))));
			sleep(2);
		elif choose == 5:
			# Show all
			show_all();
			sleep(2);
		elif choose == 6:
			# Borrow function
			print(borrow(int(input('Type ID of book to borrow: '))));
			sleep(2);
		elif choose == 7:
			# Return function
			print(return_book(int(input('Type ID of book to return: '))));
			sleep(2);
		else:
			print("Program will shutdown in 2 seconds! ");
			sleep(2);
			running = False;