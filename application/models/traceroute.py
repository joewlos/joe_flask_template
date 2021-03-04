# -*- coding: utf-8 -*-
'''
TRACEROUTE
'''
# Import required packages
from application.models.shared import db


'''
PARSING FUNCTION
'''
def parse_traceroute(raw_string):
    '''
    Parse the data and return as a dictionary
    '''
    raw_lst = raw_string.split('\n')[1:]  # Ignore first line
    hop = 0

    # Iterate across rows to find hops
    output = {}
    for row in raw_lst:
        possible_hop = row[1]
        if possible_hop != ' ':
            hop = int(possible_hop)

        # Iterate to find the ms for the hops
        splt_row = row.split('  ')
        for item in splt_row:
            if item.endswith('ms'):
                ms = float(item[:-3])

                # Add output pair to lst
                output.setdefault(hop, []).append(ms)

    # Return the output for optional storage
    return output


'''
TRACEROUTE STORAGE MODELS
'''
class TraceRouteRaw(db.Model):
    '''
    Store the raw text from a traceroute
    '''
    id = db.Column(db.Integer, primary_key=True)
    raw_string = db.Column(db.Text)

    # Relationship
    parsed = db.relationship('TraceRouteParsed', backref='trace_route_raw', lazy=True)

    # Representation
    def __repr__(self):
        return '<id %r>' % self.id
    
    # Add the raw input to the database
    def create_new_traceroute(self):
        db.session.add(self)
        db.session.commit()
        return None

    # Create relationship to parsed string in database and store
    def store_parsed_traceroute(self):

        # Parse the traceroute text
        output = parse_traceroute(self.raw_string)

        # Iterate across the keys, which are our hops
        for hop in output.keys():
            for ms in output[hop]:

                # Create a new parsed row for the hops
                parsed = TraceRouteParsed(
                    hop=hop,
                    ms=ms,
                    raw_id=self.id
                )
                db.session.add(parsed)
        
        # Commit to database
        db.session.commit()

        # Return the id
        return self.id

class TraceRouteParsed(db.Model):
    '''
    Parsed traceroute string
    '''
    id = db.Column(db.Integer, primary_key=True)
    hop = db.Column(db.Integer)
    ms = db.Column(db.Float)

    # Relationship
    raw_id = db.Column(
        db.Integer, 
        db.ForeignKey('trace_route_raw.id'),
        nullable=False
    )

    # Representation
    def __repr__(self):
        return '<id %r>' % self.id