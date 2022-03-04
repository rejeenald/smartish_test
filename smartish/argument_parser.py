
#importing argparse module
import argparse
  
class KeyValueArgumentParser(argparse.Action):
    def __call__( self , parser, namespace, values, option_string = None):
        setattr(namespace, self.dest, dict())
          
        for value in values:
            key, value = value.split('=')
            getattr(namespace, self.dest)[key] = value
  
# # creating parser object
# parser = argparse.ArgumentParser()
  
# # adding an arguments 
# parser.add_argument('--kwargs', 
#                     nargs='*', 
#                     action = keyvalue)
  
#  #parsing arguments 
# args = parser.parse_args()
  
# # show the dictionary
# print(args.kwargs)