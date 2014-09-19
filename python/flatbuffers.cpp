#include "Python.h"

#include "flatbuffers/idl.h"

PyObject* namedtuple_;
PyObject* enum_;

namespace flatbuffers {

PyObject* GetPyNamespace(PyObject* root, const Namespace& ns) {
    auto py_namespace = root;

    for(auto& component: ns.components) {
        auto current = PyDict_GetItem(py_namespace, PyString_FromString(component.c_str()));
        py_namespace = (current != nullptr) ? current : PyDict_New();
    };

    return py_namespace;
}

// PyObject* FreezePyNamespace(PyObject* root) {

PyObject* GenStruct(const Parser &parser, const StructDef &struct_def) {
  auto& fields = struct_def.fields.vec;
  auto py_fields = PyList_New(0);

  for (auto it = fields.begin(); it != fields.end(); ++it) {
    auto &field = **it;

    if(field.deprecated) continue;
    PyList_Append(py_fields, PyString_FromString(field.name.c_str()));
  }

  return PyObject_Call(namedtuple_, Py_BuildValue("(so)", struct_def.name.c_str(), py_fields), nullptr); 
}

PyObject* GeneratePython(const Parser &parser) {
  auto py_types_root = PyDict_New();
  
  for (auto it = parser.enums_.vec.begin(); it != parser.enums_.vec.end(); ++it) {
      auto &enumeration = **it;
  }

  for (auto it = parser.structs_.vec.begin();
       it != parser.structs_.vec.end(); ++it) {
      auto &structure = **it;
      auto py_namespace = GetPyNamespace(py_types_root, *structure.defined_namespace); 
      PyDict_SetItem(py_namespace, PyString_FromString(structure.name.c_str()), GenStruct(parser, structure));
  };

  return py_types_root;
}

}

PyObject* flatbuffers_load_idl(PyObject* self, PyObject* args) {
    //return PyString_FromString("hello world!");
    return PyObject_Call(namedtuple_, Py_BuildValue("(ss)", "Person", "first_name last_name"), nullptr);
}

static PyMethodDef FlatBuffersMethods[] = {
    {"load_idl", flatbuffers_load_idl, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initflatbuffers() {
    Py_InitModule("flatbuffers", FlatBuffersMethods);

    auto collections_mod = PyImport_ImportModuleEx("collections", NULL, NULL, Py_BuildValue("(ss)", "namedtuple", "defaultdict"));
    namedtuple_ = PyObject_GetAttr(collections_mod, PyString_FromString("namedtuple"));

    auto enum_mod = PyImport_ImportModuleEx("enum", NULL, NULL, Py_BuildValue("(s)", "Enum"));
    enum_ = PyObject_GetAttr(enum_mod, PyString_FromString("Enum"));
}
