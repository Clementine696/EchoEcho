import sounddevice as sd
s = sd.query_devices()
s_input = []
s_output = []
# fs = 44100
# sd.default.samplerate = fs

def show_input_device(s):
    for device in s:
        if device['max_input_channels'] > 0 and device['max_output_channels'] == 0:
            s_input.append(device)
            print("input device :" + device['name'])
        else:
            continue

def show_output_device(s):
    for device in (s):
        if device['max_input_channels'] == 0 and device['max_output_channels'] > 0:
            s_output.append(device)
            print("output device : " + device['name'])
        else:
            continue

def selected_input_device():
    print("Input available device :")  
    show_input_device(s)
    device_index_input = int(input("Select input device by index: "))
    sd.default.device = s_input[device_index_input]['name']
    print(f"Selected input device: {sd.default.device}")
    
def selected_output_device():
    print("Output available device :")  
    show_output_device(s)
    device_index_output = int(input("Select output device by index: "))
    sd.default.device = s_output[device_index_output]['name']
    print(f"Selected output device: {sd.default.device}")
    
if __name__ == "__main__":
    selected_input_device()
    selected_output_device()
    # print(s)