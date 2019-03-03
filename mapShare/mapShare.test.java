public void mapShare(){
    assert mapShare({"a": "aaa", "b": "bbb", "c": "ccc"}) == {"a": "aaa", "b": "aaa"}
    assert mapShare({"b": "xyz", "c": "ccc"}) == {"b": "xyz"}
    assert mapShare({"a": "aaa", "c": "meh", "d": "hi"}) == {"a": "aaa", "b": "aaa", "d": "hi"}
    assert mapShare({"a": "xyz", "b": "1234", "c": "yo", "z": "zzz"}) == {"a": "xyz", "b": "xyz", "z": "zzz"}
    assert mapShare({"a": "xyz", "b": "1234", "c": "yo", "d": "ddd", "e": "everything"}) == {"a": "xyz", "b": "xyz", "d": "ddd", "e": "everything"}
}