import tkinter as tk

def prediksi_prodi():
    label_hasil.config(text="Prodi Pilihan: Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi")
root.geometry("400x500") 

label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 14, "bold"))
label_judul.pack(pady=10)

lbl1 = tk.Label(root, text="Nilai Dasar Jaringan:")
lbl1.pack()
ent1 = tk.Entry(root)
ent1.pack()

lbl2 = tk.Label(root, text="Nilai Rekayasa Kebutuhan:")
lbl2.pack()
ent2 = tk.Entry(root)
ent2.pack()

lbl3 = tk.Label(root, text="Nilai Implementasi Basis Bata:")
lbl3.pack()
ent3 = tk.Entry(root)
ent3.pack()

lbl4 = tk.Label(root, text="Nilai Al-Islam Dan Kemuhammadiyahan:")
lbl4.pack()
ent4 = tk.Entry(root)
ent4.pack()

lbl5 = tk.Label(root, text="Nilai Algoritma:")
lbl5.pack()
ent5 = tk.Entry(root)
ent5.pack()

lbl6 = tk.Label(root, text="Nilai Pancasila:")
lbl6.pack()
ent6 = tk.Entry(root)
ent6.pack()

lbl7 = tk.Label(root, text="Nilai Kewarganegaraan :")
lbl7.pack()
ent7 = tk.Entry(root)
ent7.pack()

lbl8 = tk.Label(root, text="Nilai Matematika:")
lbl8.pack()
ent8 = tk.Entry(root)
ent8.pack()

lbl9 = tk.Label(root, text="Nilai Dasar Teknologi:")
lbl9.pack()
ent9 = tk.Entry(root)
ent9.pack()

lbl10 = tk.Label(root, text="Nilai Sejarah:")
lbl10.pack()
ent10 = tk.Entry(root)
ent10.pack()


btn_prediksi = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi)
btn_prediksi.pack(pady=15)

label_hasil = tk.Label(root, text="", font=("Arial", 12, "italic"), fg="blue")
label_hasil.pack(pady=5)

root.mainloop()