# program pendaftaran kursus online
umur = int(input('Berapa usia Anda sekarang: '))
if umur >= 21:
    status = str(input("Apakah Anda sudah lulus ujian kualifikasi ? (Y/T): "))
    if status.upper() == 'Y':
        print("Anda dapat mendaftar di kursus ini")
    elif status.upper() == 'T':
        print("Anda tidak dapat mendaftar di kursus ini")
else:
    print("Anda tidak memenuhi syarat")
