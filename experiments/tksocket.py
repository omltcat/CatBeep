def eleve2():


quitterMDPeleve()
global eleve2
eleve2 = tk.Tk()
eleve2.title("Espace élèves")
eleve2.config(bg='#A26F65')
eleve2.geometry('1650x1050')

global logRec

logRec = tk.Text(eleve2, width=25, height=20, takefocus=0, font = ('Tw Cen MT', 15))
logRec.place(x=400, y=310, anchor='w')

global threadEl

threadEl = threading.Thread(target=verifsock)
threadEl.daemon = True # without the daemon parameter, the function in parallel will continue even your main program ends
threadEl.start()

eleve2.mainloop()



def verifsock():
global socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('172.16.2.220', 15555))
while True:

    socket.listen(5)
    client, address = socket.accept()
    print ("{} connected".format( address ))

    response = client.recv(255)
    response2 = response.decode("utf-8")
    if response2 != "":
        logRec.insert(END, str(response2)+"\n")
    else:
        return
