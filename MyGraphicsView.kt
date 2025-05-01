package com.example.termall

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.view.View

class MyGraphicsView(context: Context) : View(context) {
    private val paint = Paint()

    override fun onDraw(canvas: Canvas) {
        super.onDraw(canvas)

        // Background color
        canvas.drawColor(Color.WHITE)

        // Set paint properties
        paint.color = Color.BLUE
        paint.style = Paint.Style.FILL

        // Draw a circle
        canvas.drawCircle(300f, 300f, 150f, paint)

        // Draw a line
        paint.color = Color.RED
        paint.strokeWidth = 10f
        canvas.drawLine(100f, 600f, 600f, 600f, paint)

        // Draw text
        paint.color = Color.BLACK
        paint.textSize = 60f
        canvas.drawText("Simple Graphics!", 100f, 750f, paint)
    }
}
