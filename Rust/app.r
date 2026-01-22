# Aplikasi Kalkulator Sederhana menggunakan R Shiny
# Jalankan file ini dengan: shiny::runApp()

library(shiny)

ui <- fluidPage(
  titlePanel("Kalkulator Sederhana"),
  sidebarLayout(
    sidebarPanel(
      numericInput("num1", "Angka pertama:", value = 0),
      numericInput("num2", "Angka kedua:", value = 0),
      selectInput(
        "operator",
        "Pilih operasi:",
        choices = c(
          "Tambah (+)" = "+",
          "Kurang (-)" = "-",
          "Kali (*)"   = "*",
          "Bagi (/)"   = "/"
        )
      ),
      actionButton("hitung", "Hitung")
    ),
    mainPanel(
      h3("Hasil:"),
      verbatimTextOutput("hasil")
    )
  )
)

server <- function(input, output) {
  hasil_perhitungan <- eventReactive(input$hitung, {
    a <- input$num1
    b <- input$num2

    switch(input$operator,
           "+" = a + b, # nolint: indentation_linter.
           "-" = a - b,
           "*" = a * b,
           "/" = if (b == 0) "Error: pembagian dengan nol" else a / b
    )
  })

  output$hasil <- renderText({
    hasil_perhitungan()
  })
}

shinyApp(ui = ui, server = server)
