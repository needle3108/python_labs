#include <Python.h>
#include"funkcja.h"
#include"nwd.h"
//mozliwe sygnatury funkcji stanowiącej "interfejs" pomiędzy pythonem i C
//static PyObject *mod_met(PyObject *self){
//static PyObject *mod_met(PyObject *self, PyObject *args, PyObject *kw){
static PyObject *mod_met(PyObject *self, PyObject *args){
	int a,b;
	int c = 0;
	PyObject *d = NULL;

	if(!PyArg_ParseTuple(args, "ii|iO", &a, &b, &c, &d)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	int s=a+b+c;
	if(d){
		int r=PyList_Size(d);
		for(int i=0; i<r; i++){
			s+=PyLong_AsLong(PyList_GetItem(d, i));
		}
	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", s);
}

static PyObject *mod_sort(PyObject *self, PyObject *args){
	PyObject *a = NULL;

	if(!PyArg_ParseTuple(args, "O", &a)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}

	int tab[PyList_Size(a)];
	for(int i=0; i<PyList_Size(a); i++){
		tab[i] = PyLong_AsLong(PyList_GetItem(a, i));
	}

	int size = PyList_Size(a);
	sort(tab, size);

	for(int i=0; i<size; i++){
		PyList_SetItem(a, i, PyLong_FromLong(tab[i]));
	}

	return a;
}

static PyObject *mod_dict(PyObject *self, PyObject *args){
	PyObject *a = NULL;
	PyObject *d = PyDict_New();

	if(!PyArg_ParseTuple(args, "O", &a)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}

	PyObject *key, *value;
	Py_ssize_t pos = 0;

	while(PyDict_Next(a, &pos, &key, &value)){
		PyObject *ke = PyTuple_New(2);
		int v = PyLong_AsLong(value);
		int k = PyLong_AsLong(key);

		int nwd = NWD(v, k);
		PyTuple_SetItem(ke, 0, v);
		PyTuple_SetItem(ke, 1, k);

		PyDict_SetItem(d, ke, PyLong_FromLong(nwd));
	}

	return d;
}

//tablica metod
static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."}, 
	{"sort", (PyCFunction)mod_sort, METH_VARARGS, "Funkcja ..."},
	{"dict", (PyCFunction)mod_dict, METH_VARARGS, "Funkcja ..."},
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}
