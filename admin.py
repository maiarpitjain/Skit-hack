
import create_100_images
ch=int(input("Enter number of students whose data would you want to add in your database"))

#create_100_images.create_name_in_db()
create_100_images.create_ch_folder(ch)
create_100_images.take_100_images(ch)

