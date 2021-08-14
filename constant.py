PORT = 5050
PATH = 'C:/Users/Santiago/Desktop/proyecto_Telematica/server_files/'

LIST_ALL = 'ALL'                # Lists everything                        
CREATE_BUCKET = 'CBUCKET'       # Create a new bucket                     
DELETE_BUCKET = 'DBUCKET'       # Delete a selected bucket                 
LIST_BUCKETS = 'LBUCKET'        # List all buckets                         
LIST_FILES = 'LFILE'            # List all files of an existing bucket   
UPLOAD_FILE = 'UPFILE'          # Upload a file to the server             
DOWNLOAD_FILE = 'DWFILE'        # Download a file from the server          
DELETE_FILE = 'DFILE'          # Delete a file from an existing bucket   
DISCONNECT_COMMAND = 'EXIT'     # Disconnects from server        
TRAVEL_PATH = 'CD'
BACK = 'BK'
HELP = 'HELP'

COMMAND_MESSAGE = {
    100: 'BUCKET CREATED',
    101: 'FILE CREATED',
    200: 'BUCKET DELETED',
    201: 'FILE DELETED',
    300: 'UNKNOWN COMMAND',
    301: 'TOO MANY ARGUMENTS',
    302: 'NOT ENOUGH ARGUMENTS',
    303: 'INVALID ARGUMENTS',
    304: 'BUCKET NOT FOUND',
    305: 'FILE NOT FOUND',
    306: 'FILE ALREADY EXISTS',
    307: 'BUCKET ALREADY EXISTS',
    400: 'FILE UPLOADED',
    401: 'FAILED TO UPLOAD',
    402: 'FILE DOWNLOADED',
    403: 'FAILED TO DOWNLOAD',
    500: 'LIST OBTAINED',
    600: 'DISCONNECTED',
}
