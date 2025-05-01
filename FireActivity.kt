package com.example.termall

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.google.firebase.database.FirebaseDatabase

class FireActivity : AppCompatActivity() {

    private lateinit var nameInput: EditText
    private lateinit var emailInput: EditText
    private lateinit var saveButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_fire)

        nameInput = findViewById(R.id.nameInput)
        emailInput = findViewById(R.id.emailInput)
        saveButton = findViewById(R.id.saveButton)

        saveButton.setOnClickListener {
            saveUserToFirebase()
        }
    }

    private fun saveUserToFirebase() {
        val name = nameInput.text.toString().trim()
        val email = emailInput.text.toString().trim()

        if (name.isEmpty() || email.isEmpty()) {
            Toast.makeText(this, "Fill in both fields", Toast.LENGTH_SHORT).show()
            return
        }

        val user = User(name, email)

        val database = FirebaseDatabase.getInstance("https://labenviron-4f581-default-rtdb.firebaseio.com/"
        )
        val usersRef = database.getReference("users")

        val userId = usersRef.push().key!!
        usersRef.child(userId).setValue(user)
            .addOnSuccessListener {
                Toast.makeText(this, "Saved to Firebase", Toast.LENGTH_SHORT).show()
                nameInput.text.clear()
                emailInput.text.clear()
            }
            .addOnFailureListener {
                Toast.makeText(this, "Failed: ${it.message}", Toast.LENGTH_SHORT).show()
            }
    }
}
