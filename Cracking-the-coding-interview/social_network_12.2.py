'''

Python implementation of the following problem in Cracking The Coding Interview.
	- I implemented classed to represent different machines and methods to search through them
	- Didn't implement a full BFS algo with shortest path, but check my github it's there.

How would you design the data structures for a very large social network (Facebook,
LinkedIn, etc)? Describe how you would design an algorithm to show the connection,
or path, between two people (e g , Me -> Bob -> Susan -> Jason -> You)

Object Oriented design :

'*' are for attributes
'-' are for mehtods

server
* list of machines

machine
* machine ID
* list of persons
- add / delete person
- get person's list of friends (given the person ID)

person
* person ID
* list of person ID (friends)
- add / delete friend

To access a friends's friends.
1. find the machine this friend is on
2. Access this machine
3. get the person's list friends


'''

class Server:

	def __init__(self, machines=[]):
		self.list_of_machines = machines

class Machine:

	def __init__(self, machine_id, persons=[]):
		self.machine_id = machine_id
		self.list_of_persons = persons

class Person:

	def __init__(self, person_id, name, gender, city, friends = []):
		self.person_id = person_id
		self.name = name
		self.gender = gender
		self.city = city
		self.friends = friends


person_1 = Person(1,'Nicolas','M','Paris', [2,3])
person_2 = Person(2,'Caroline','F','Singapore',[1])
machine_A = Machine('A',[person_1,person_2])

person_3 = Person(3,'Benoit','M','Bangaluru',[1])
machine_B = Machine('B',[person_3])

server = Server([machine_A, machine_B])

'''
# quick test
for machine in server.list_of_machines:
    for i in range(len(machine.list_of_persons)):
    	print machine.list_of_persons[i].name
'''    	

def pick_machine(person_id, server):
	''' given a person id, returns the corresponding machine '''
	for machine in server.list_of_machines:
		for person in machine.list_of_persons:
			if person_id == person.person_id:
				return machine

def pick_person_in_machine(person_id, machine):
	''' given a person id, return the correspond person'''
	for person in machine.list_of_persons:
		if person_id == person.person_id:
			return person

def get_person_list_of_friends(person_id):

	current_id = person_id

	current_machine = pick_machine(current_id, server)
	current_person = pick_person_in_machine(current_id, current_machine) 
	friends_of_current_person = current_person.friends

	return friends_of_current_person	


### Go from one friend to another, by switching machine if need be.
	# I'm given the server that hosts everything and a start ID

current_id = 1 # start at Nicolas
 
friends_of_current_person = get_person_list_of_friends(current_id)

stack_of_persons_to_explore = []
for friend in friends_of_current_person:
	stack_of_persons_to_explore.append(friend)

# repeat

current_id = stack_of_persons_to_explore.pop()

friends_of_current_person = get_person_list_of_friends(current_id)

stack_of_persons_to_explore = []
for friend in friends_of_current_person:
	stack_of_persons_to_explore.append(friend)

print current_id # It's #3, Benoit, which is on a different machine.
