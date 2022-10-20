from fplib import fplib

# fingerprint module variables
fp = fplib(port=0, baud=115200, ledpin=25, timeout=3)

# module initializing
init = fp.init()
print("is initialized :", init)

# Run only task that is specified
task = 1

#=#=# ---------------------------- T.A.S.K.S ---------------------------------- #=#=#
# 1. turning ON & OFF LED
if task == 1:
   # ON
   led = fp.set_led(True)
   print("\n |__ LED status :", led) 

   utime.sleep(2)

   led = fp.set_led(False)
   print("\n |__ LED status :", led)
     
# 2. check if finger is pressed or not
if task == 2:
    pressed = fp.is_finger_pressed()
    print("\n |__ is finger pressed ?", pressed)
    
# 3. make fingerprint template
if task == 3:
    data, downloadstat =fp.MakeTemplate()
    print(f"\n |__ Is template fetched ?", downloadstat)
    
    img_arr = []
    if downloadstat:
        data = bytearray(data)
        for ch in data:
            img_arr.append(ch)
    print("fetched template data: ", img_arr)

# 4. enroll fingerprint to device memory
if task == 4:
    if fp.is_finger_pressed():
        # Checking for finger press 
        print("\n |__Finger is pressed")
        # Starting enrollment 
        id, data, downloadstat = fp.enroll()
        print(f"\n |__ID: {id} & is captured ?", data != None)
        # To get total enrollment count
        print(f"\n |__ enrolled counts :", fp.get_enrolled_cnt())
        
# 5. delete saved template from device (delite all/ delete by id)
if task == 5:
    #status = fp.delete(idx=0) # delete by id
    status = fp.delete() # delete all
    print("\n |__ Delete status: ", status)
    # To get total enrollment count
    print(f"\n |__ enrolled counts :", fp.get_enrolled_cnt())
    
# 6. identify / recognize fingerprint
if task == 6:
    id = fp.identify()
    print("\n |__ identified id:", id)
    
# 7. settemplate - set a template data to device
if task == 7:
    DATA = [] # a 502 length python list, that we get after running "task 3"
    fp.delete(idx=0)
    status = fp.setTemplate(idx=0, data=DATA)
    print("\n |__ set template status :", status)
