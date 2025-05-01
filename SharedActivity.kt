package com.example.termall

import android.content.Context
import android.content.SharedPreferences
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.termall.R

class SharedActivity : AppCompatActivity() {

    private lateinit var nameEditText: EditText
    private lateinit var ageEditText: EditText
    private lateinit var saveButton: Button
    private lateinit var loadButton: Button
    private lateinit var displayTextView: TextView

    // SharedPreferences instance
    private lateinit var sharedPreferences: SharedPreferences

    // Key constants for SharedPreferences
    companion object {
        const val PREF_NAME = "UserPrefs"
        const val KEY_NAME = "username"
        const val KEY_AGE = "age"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_shared)

        nameEditText = findViewById(R.id.nameEditText)
        ageEditText = findViewById(R.id.ageEditText)
        saveButton = findViewById(R.id.saveButton)
        loadButton = findViewById(R.id.loadButton)
        displayTextView = findViewById(R.id.displayTextView)

        // Initialize SharedPreferences
        sharedPreferences = getSharedPreferences(PREF_NAME, Context.MODE_PRIVATE)

        saveButton.setOnClickListener {
            saveData()
        }

        loadButton.setOnClickListener {
            loadData()
        }
    }

    private fun saveData() {
        val username = nameEditText.text.toString()
        val age = ageEditText.text.toString()

        if (username.isNotEmpty() && age.isNotEmpty()) {
            // Saving data in SharedPreferences
            val editor = sharedPreferences.edit()
            editor.putString(KEY_NAME, username)
            editor.putString(KEY_AGE, age)
            editor.apply()  // Commit the changes

            Toast.makeText(this, "Data Saved!", Toast.LENGTH_SHORT).show()
        } else {
            Toast.makeText(this, "Please enter valid data", Toast.LENGTH_SHORT).show()
        }
    }

    private fun loadData() {
        // Retrieving data from SharedPreferences
        val username = sharedPreferences.getString(KEY_NAME, "No name found")
        val age = sharedPreferences.getString(KEY_AGE, "No age found")

        // Display the saved data
        displayTextView.text = "Name: $username\nAge: $age"
    }
}
