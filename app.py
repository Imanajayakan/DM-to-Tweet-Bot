from twitter import Twitter
import time

tw = Twitter()

def start():
    print("Starting program...")
    dms = list()
    while True:
        if len(dms) != 0:
            for i in range(len(dms)):
                message = dms[i]["message"]
                sender_id = dms[i]["sender_id"]
                id = dms[i]["id"]
                
                if len(message) != 0 and len(message) < 280:
                    if "Test" in message:
                        message = message.replace("Test", "")
                        if len(message) != 0:
                            if dms[i]['media'] is None:
                                print("DM will be posted")
                                tw.post_tweet(message)
                                tw.delete_dm(id)
                                #post twitter here
                            else:
                                print("DM will be posted with media")
                                tw.post_media(message,dms[i]['media'])
                                tw.delete_dm(id)
                            
                        else:
                            print("DM deleted because it's empty..")
                            tw.delete_dm(id)
                            #delete DM here
                            
                    else:
                        print("DM will be deleted because doesn't have the right keyword")
                        tw.delete_dm(id)
                        #delete DM
            dms = list()
            
        else:
            print("Direct Message is empty...")
            dms = tw.read_dm()
            if len(dms) == 0:
                time.sleep(30)
                
if __name__ == "__main__":
    start()