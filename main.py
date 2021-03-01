from PySide6 import *
import currency_converter

class App(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()
		self.c = currency_converter.CurrencyConverter()
		self.setWindowTitle("Convertisseur de devises")
		self.setup() 
		self.style_css() 
		self.set_default_values()
		self.connections()
	
	def setup(self):
		
		self.layout = QtWidgets.QHBoxLayout(self)
		
		self.cbb_devisesFrom = QtWidgets.QComboBox() 
		self.spn_montant = QtWidgets.QSpinBox() 
		self.cbb_devisesTo = QtWidgets.QComboBox() 
		self.spn_montantConverti = QtWidgets.QSpinBox() 
		self.btn_inverser = QtWidgets.QPushButton("Inverser devises")
		
		self.layout.addWidget(self.cbb_devisesFrom)
		self.layout.addWidget(self.spn_montant)
		self.layout.addWidget(self.cbb_devisesTo)
		self.layout.addWidget(self.spn_montantConverti)
		self.layout.addWidget(self.btn_inverser)
	
	def style_css(self):	
		self.btn_inverser.setStyleSheet("background-color: red")
	
	def set_default_values(self):

		self.cbb_devisesFrom.addItems(sorted(list(self.c.currencies)))
		self.cbb_devisesTo.addItems(sorted(list(self.c.currencies)))

		self.cbb_devisesFrom.setCurrentText("EUR")
		self.cbb_devisesTo.setCurrentText("EUR")
		
		self.spn_montant.setRange(0,1000000)
		self.spn_montantConverti.setRange(0,1000000)

		self.spn_montant.setValue(1)
		self.spn_montantConverti.setValue(1)
	
	def connections(self):

		self.cbb_devisesFrom.activated.connect(self.compute)
		self.cbb_devisesTo.activated.connect(self.compute)

		self.spn_montant.valueChanged.connect(self.compute)
		self.spn_montantConverti.valueChanged.connect(self.compute)
		
		self.btn_inverser.clicked.connect(self.inverser)
	
	def compute(self):

		montant = self.spn_montant.value() 
		devise_from = self.cbb_devisesFrom.currentText() 
		devise_to = self.cbb_devisesTo.currentText()
		
		try :
			resultat = self.c.convert(montant, devise_from, devise_to)
		
		except currency_converter.currency_converter.RateNotFoundError :
			print("not found convertion")
		
		else :
			self.spn_montantConverti.setValue(resultat)
	
	def inverser(self):		
		devise_from = self.cbb_devisesFrom.currentText()
		devise_to = self.cbb_devisesTo.currentText()
		
		self.cbb_devisesFrom.setCurrentText(devise_to)
		self.cbb_devisesTo.setCurrentText(devise_from)
		
		self.compute()

# create an application PySide
app = QtWidgets.QApplication([])

# create a window on my app
win = App()
win.show()

# execute the app
app.exec_()