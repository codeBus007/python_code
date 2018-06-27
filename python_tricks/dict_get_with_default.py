# coding: utf-8

name_for_userid = {
	382: "Alice",
	590: "Bob",
	911: "Hellen"
}

def greeting(user_id):
	print(f"Hi, {name_for_userid.get(user_id, 'there')}")

greeting(911)
greeting(119)
