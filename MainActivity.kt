package com.example.appterm

import android.app.NotificationChannel
import android.app.NotificationManager
import android.os.Build
import android.os.Bundle
import android.view.*
import android.widget.Button
import android.widget.PopupMenu
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.widget.Toolbar
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat

class MainActivity2 : AppCompatActivity() {

    private lateinit var contextTextView: TextView
    private lateinit var popupButton: Button
    private lateinit var notifyButton: Button

    private val CHANNEL_ID = "demo_channel_id"
    private val NOTIFICATION_ID = 1

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val toolbar = findViewById<Toolbar>(R.id.toolba)
        setSupportActionBar(toolbar)

        contextTextView = findViewById(R.id.context_tex)
        popupButton = findViewById(R.id.popup_butto)
        notifyButton = findViewById(R.id.notify_button)

        // Register context menu for TextView
        registerForContextMenu(contextTextView)

        // Show popup menu on button click
        popupButton.setOnClickListener {
            val popup = PopupMenu(this, it)
            popup.menuInflater.inflate(R.menu.popup_menu, popup.menu)
            popup.setOnMenuItemClickListener { item ->
                when (item.itemId) {
                    R.id.option_one -> showToast("Popup: Option 1 selected")
                    R.id.option_two -> showToast("Popup: Option 2 selected")
                }
                true
            }
            popup.show()
        }

        // Create notification channel
        createNotificationChannel()

        // Request notification permission (Android 13+)
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            requestPermissions(arrayOf(android.Manifest.permission.POST_NOTIFICATIONS), 100)
        }

        // Show notification on button click
        notifyButton.setOnClickListener {
            val builder = NotificationCompat.Builder(this, CHANNEL_ID)
                .setSmallIcon(android.R.drawable.ic_dialog_info)
                .setContentTitle("EventHub+ Alert")
                .setContentText("You clicked the notification button!")
                .setPriority(NotificationCompat.PRIORITY_HIGH)

            with(NotificationManagerCompat.from(this)) {
                notify(NOTIFICATION_ID, builder.build())
            }
        }
    }

    // Inflate Options Menu
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    // Handle Options Menu
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.action_settings -> {
                showToast("Options Menu: Settings selected")
                true
            }
            R.id.action_about -> {
                showToast("Options Menu: About selected")
                true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }

    // Create Context Menu
    override fun onCreateContextMenu(menu: ContextMenu?, v: View?, menuInfo: ContextMenu.ContextMenuInfo?) {
        super.onCreateContextMenu(menu, v, menuInfo)
        if (v?.id == R.id.context_tex) {
            menuInflater.inflate(R.menu.context_menu, menu)
        }
    }

    // Handle Context Menu
    override fun onContextItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.context_edit -> {
                showToast("Context Menu: Edit selected")
                true
            }
            R.id.context_delete -> {
                showToast("Context Menu: Delete selected")
                true
            }
            else -> super.onContextItemSelected(item)
        }
    }

    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val name = "Demo Channel"
            val descriptionText = "Channel for button click notification"
            val importance = NotificationManager.IMPORTANCE_HIGH
            val channel = NotificationChannel(CHANNEL_ID, name, importance).apply {
                description = descriptionText
            }
            val notificationManager: NotificationManager =
                getSystemService(NotificationManager::class.java)
            notificationManager.createNotificationChannel(channel)
        }
    }

    private fun showToast(message: String) {
        Toast.makeText(this, message, Toast.LENGTH_SHORT).show()
    }
}
