package com.example.termall

import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper

class DatabaseHelper(context: Context) : SQLiteOpenHelper(context, DATABASE_NAME, null, DATABASE_VERSION) {

    companion object {
        private const val DATABASE_NAME = "userDatabase.db"
        private const val DATABASE_VERSION = 1
        const val TABLE_NAME = "users"
        const val COLUMN_ID = "_id"
        const val COLUMN_NAME = "name"
        const val COLUMN_AGE = "age"
    }

    override fun onCreate(db: SQLiteDatabase?) {
        val createTableSQL = "CREATE TABLE $TABLE_NAME (" +
                "$COLUMN_ID INTEGER PRIMARY KEY AUTOINCREMENT, " +
                "$COLUMN_NAME TEXT, " +
                "$COLUMN_AGE INTEGER)"
        db?.execSQL(createTableSQL)
    }

    override fun onUpgrade(db: SQLiteDatabase?, oldVersion: Int, newVersion: Int) {
        db?.execSQL("DROP TABLE IF EXISTS $TABLE_NAME")
        onCreate(db)
    }
}
