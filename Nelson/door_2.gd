extends Area2D


func _on_body_entered(body):
	if body.is_in_group("Players"):
		get_tree().change_scene_to_file("res://Level 3.tscn")
