#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # Prep empty list to store routes/ empty hash table for lookups
    route = [None] * length
    hash_table = {}

    for ticket in tickets: # list name given for test
        # Save destinations to the hash table {source, destination}
        hash_table[ticket.source] = ticket.destination

    # Instantiate next location using NONE as the key
    next_location = hash_table['NONE']

    # Loop through
    for i in range(0, length):
        # Put first index value into route list
        route[i] = next_location
        # Set next key to be that value
        next_location = hash_table[next_location]

    return route

if __name__ == "__main__":
    ticket_1 = Ticket("PIT", "ORD")
    ticket_2 = Ticket("XNA", "CID")
    ticket_3 = Ticket("SFO", "BHM")
    ticket_4 = Ticket("FLG", "XNA")
    ticket_5 = Ticket("NONE", "LAX")
    ticket_6 = Ticket("LAX", "SFO")
    ticket_7 = Ticket("CID", "SLC")
    ticket_8 = Ticket("ORD", "NONE")
    ticket_9 = Ticket("SLC", "PIT")
    ticket_10 = Ticket("BHM", "FLG")

    tickets = [
        ticket_1,
        ticket_2,
        ticket_3,
        ticket_4,
        ticket_5,
        ticket_6,
        ticket_7,
        ticket_8,
        ticket_9,
        ticket_10,
    ]

    print(reconstruct_trip(tickets, 10))

