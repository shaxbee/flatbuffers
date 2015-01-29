# automatically generated by the FlatBuffers compiler, do not modify

import flatbuffers
import enum
import operator
import struct

# localize performance sensitive globals
_getitem = operator.getitem
_tuple = tuple
_Enum = enum.Enum


class FromInclude(_Enum):
    IncludeVal = 0


def read_FromInclude(view, offset):
    return FromInclude(flatbuffers.encode.read_long(view, offset))


class Color(_Enum):
    Red = 1
    Green = 2
    Blue = 8


def read_Color(view, offset):
    return Color(flatbuffers.encode.read_byte(view, offset))


class Any(_Enum):
    NONE = 0
    Monster = 1


def read_Any(view, offset):
    return Any(flatbuffers.encode.read_ubyte(view, offset))


class Test(flatbuffers.Struct):
    _FORMAT = struct.Struct("hbx")

    @classmethod
    def format(cls):
        return cls._FORMAT

    def get_a(self):
        return _getitem(self, 0)

    def get_b(self):
        return _getitem(self, 1)


class Vec3(flatbuffers.Struct):
    _FORMAT = struct.Struct("fff4xdbxhbx2x")

    @classmethod
    def format(cls):
        return cls._FORMAT

    def get_x(self):
        return _getitem(self, 0)

    def get_y(self):
        return _getitem(self, 1)

    def get_z(self):
        return _getitem(self, 2)

    def get_test1(self):
        return _getitem(self, 3)

    def get_test2(self):
        return Color(_getitem(self, 4))

    def get_test3(self):
        return _tuple.__new__(Test, _getitem(self, slice(5, 7)))


class Stat(flatbuffers.Table):
    def get_id(self):
        offset = self.get_offset(0)
        if offset == 0:
            return None
        data_offset = self._offset + offset
        data_offset += flatbuffers.encode.read_uoffset(self._buf, data_offset)
        return flatbuffers.encode.read_string(self._buf, data_offset)

    def get_val(self):
        return self.read_long_field(1, 0)


class StatBuilder(object):
    def __init__(self, fbb, start):
        self._fbb = fbb
        self._start = start

    def add_id(self, value):
        assert type(value) is Offset
        self.add_offset(0, value, 0)

    def add_val(self, value):
        self.add_long(1, value, 0)

class Monster(flatbuffers.Table):
    def get_pos(self):
        offset = self.get_offset(0)
        if offset == 0:
            return None
        data_offset = self._offset + offset
        return Vec3(self._buf, data_offset)

    def get_mana(self):
        return self.read_short_field(1, 150)

    def get_hp(self):
        return self.read_short_field(2, 100)

    def get_name(self):
        offset = self.get_offset(3)
        if offset == 0:
            return None
        data_offset = self._offset + offset
        data_offset += flatbuffers.encode.read_uoffset(self._buf, data_offset)
        return flatbuffers.encode.read_string(self._buf, data_offset)

    def get_inventory(self):
        offset = self.get_offset(5)
        if offset == 0:
            return None
        data_offset = self._offset + offset
        return flatbuffers.encode.read_scalar_vector("B", self._buf, data_offset)

    def get_color(self):
        return self.read_field(6, read_Color, 8)

    def get_test_type(self):
        return self.read_field(7, read_Any, 0)

    def get_test(self):
        tpe = self.get_test_type()
        if tpe is None or tpe == Any.NONE:
            return None
        if tpe == Any.Monster:
            target = Monster
        offset = self.get_offset(8)
        if offset == 0:
            return None
        data_offset = self._offset + offset
        data_offset += flatbuffers.encode.read_uoffset(self._buf, data_offset)
        return target(self._buf, data_offset)

    def get_test4(self):
        offset = self.get_offset(9)
        if offset == 0:
            return None
        data_offset = self._offset + offset
        return flatbuffers.StructVector(Test, self._buf, data_offset)

    def get_testarrayofstring(self):
        offset = self.get_offset(10)
        if offset == 0:
            return None
        data_offset = self._offset + offset
        return flatbuffers.IndirectVector(flatbuffers.encode.read_string, self._buf, data_offset)

    def get_testarrayoftables(self):
        """
         an example documentation comment: this will end up in the generated code
         multiline too
        """

        offset = self.get_offset(11)
        if offset == 0:
            return None
        data_offset = self._offset + offset
        return flatbuffers.IndirectVector(Monster, self._buf, data_offset)

    def get_enemy(self):
        offset = self.get_offset(12)
        if offset == 0:
            return None
        data_offset = self._offset + offset
        data_offset += flatbuffers.encode.read_uoffset(self._buf, data_offset)
        return Monster(self._buf, data_offset)

    def get_testnestedflatbuffer(self):
        offset = self.get_offset(13)
        if offset == 0:
            return None
        data_offset = self._offset + offset
        return flatbuffers.encode.read_scalar_vector("B", self._buf, data_offset)

    def get_testempty(self):
        offset = self.get_offset(14)
        if offset == 0:
            return None
        data_offset = self._offset + offset
        data_offset += flatbuffers.encode.read_uoffset(self._buf, data_offset)
        return Stat(self._buf, data_offset)


class MonsterBuilder(object):
    def __init__(self, fbb, start):
        self._fbb = fbb
        self._start = start

    def add_pos(self, value):
        assert type(value) is Offset
        self.add_offset(0, value, 0)

    def add_mana(self, value):
        self.add_short(1, value, 150)

    def add_hp(self, value):
        self.add_short(2, value, 100)

    def add_name(self, value):
        assert type(value) is Offset
        self.add_offset(3, value, 0)

    def add_inventory(self, value):
        assert type(value) is Offset
        self.add_offset(5, value, 0)

    def add_color(self, value):
        assert type(value) is Color
    def add_test(self, value):
        assert type(value) is Any
    def add_test4(self, value):
        assert type(value) is Offset
        self.add_offset(9, value, 0)

    def add_testarrayofstring(self, value):
        assert type(value) is Offset
        self.add_offset(10, value, 0)

    def add_testarrayoftables(self, value):
        assert type(value) is Offset
        self.add_offset(11, value, 0)

    def add_enemy(self, value):
        assert type(value) is Offset
        self.add_offset(12, value, 0)

    def add_testnestedflatbuffer(self, value):
        assert type(value) is Offset
        self.add_offset(13, value, 0)

    def add_testempty(self, value):
        assert type(value) is Offset
        self.add_offset(14, value, 0)

def get_root_as_Monster(source):
    buf = source if type(source) is memoryview else memoryview(source)
    offset = flatbuffers.encode.read_uoffset(buf, 0)
    return Monster(buf, offset)
