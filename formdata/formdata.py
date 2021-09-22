import json
import os      
        
class FormData:
     """
     FormData is a data convertion programme written using Python Programming Language.
     
     """
     
     def __init__(self, obj):
        """
          -obj(type => str): data Format to covert to.
                         obj= "json" for json file format
                         obj= "csv" for CSV file format
          e.g.
          > data = FormData(obj="json")
          > print(data.json_csv)
          or
          > print(data.csv_json)
        """
        self.csvjson = self.C2Json(obj)
        self.jsoncsv = self.J2CSV(obj)
        self.csv_json = self.csv_json()
        self.json_csv = self.json_csv()
        self.obj = obj
     	
     @property
     def save(self):
     	return self.obj
     	
     @save.setter
     def save(self, loc, fmt):
          with open(loc, "w") as sv:
               cont=sv.write(save(os.path.join(loc, f"data.{fmt}")))

     def csv_json(self):
     	return self.csvjson.json()
     	
     def json_csv(self):
     	return self.jsoncsv.csv()
     
     def dumpJSON(self, loc, fmt="json"):
          return self.save
          #save.loc = loc
          #save(loc = 'data.json', fmt = fmt)
     	
     def dumpCSV(self, loc, fmt="csv"):
     	save.loc = data.csv
     	save.fmt = fmt
     	return save.loc
     	
     class C2Json:
        	
        	def __init__(self, obj, fp='data.csv',  delimiter=","):
        		self.obj = obj
        		self.fp= fp
        		self.delimiter = delimiter
        	
        	@property
        	def file(self):
        	     	with open(self.fp) as fps:
        	     		return fps.readlines()
        	
        	@file.setter
        	def file(self, delim,  *col):
        	    with open(self.fp) as fps:
        		    fps.write(delim.join(col))
        	
        	@file.deleter
        	def file(self):
        		os.remove(self.fp)
        	
        	def json(self):
        	       reader = self.file
        	       header = reader[0].strip().split(self.delimiter)
        	       dd = []
        	       body = reader[1:]
        	       p = [i.strip().split(",")  for i in body]
        	       for p in body:
        	       	pu = p.strip().split(",")
        	       	d ={}
        	       	for i, q in enumerate(pu):
        	       		d[header[i]] = q
        	       		dd.append(d)
        	       data = [ {self.obj : dd}]
        	       return json.dumps(data)
        	       
     class J2CSV:
            """
            Me
            """
            def __init__(self, obj,  fp="data.json"):
                self.fp = fp
                self.obj =obj
             
            @property
            def file(self):
            	with open(self.fp, "r") as fps:
            		pl = json.loads(fps.read())
            		return pl[0][self.obj]
            		
            @file.setter
            def file(self):
            	with open(self.fp) as fps:
            		return fps.read()
            		
            @file.deleter
            def file(self):
            	os.remove(self.fp)
            
            def csv(self):
            	"""
            	me
            	"""
            	js = self.file
            	head = js[0].keys()
            	for j in js:
            		k = tuple(j.items())
            	print(tuple(head))
            	print(tuple(j.values()))

p=FormData(obj="csv")
q = FormData(obj="csv")#.J2CSV(obj="csv")
#s = Store(hdr_exists=True, hdr=['col1', 'col2'])
#print(p.csv_json)
print(q.json_csv)
print(p.csv_json)
print(p.dumpJSON("data.json"))
#t=Header('col1', 'col2', 'col3')
#print(t)
