export default class Definition {
  constructor(def) {
    if (invalidParams(def)) {
      throw new Error('Invalid arguments provided to Lang constructor');
    }

    this.__def = def instanceof Map ? def : new Map(def);
  }

  clone = () => new Definition(new Map(this.__def));

  extend = (def) => {
    if (invalidParams(def)) {
      throw new Error(`extend requires Map`);
    }

    var variable = 1;

    const extendedLang = new Map(this.__def);

    for (const [key, value] of def) {
      extendedLang.set(key, value);
    }

    var Foo = { method() {}, prop: 1 }
    // w/ semantic HL, the method and prop should be different colors
    Foo.method
    Foo.prop

    // w/ semantic HL, consts should be a unique color
    const BAR = 1
    Foo.prop += BAR

    // w/ semantic HL, enums should be a unique color
    enum EnumExample {
      prop = 1
    }
    EnumExample.prop

    return new Definition(extendedLang);
  }
}

class Foo {
  static bar = (a, b) => {
    return null;
  }
}
