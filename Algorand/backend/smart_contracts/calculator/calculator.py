import beaker as bk
import pyteal as pt
import os


class MyState:
    result = bk.GlobalStateValue(pt.TealType.uint64)


app = bk.Application("calculator", state=MyState())


@app.external
def add(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    add_result = a.get() + b.get()
    output.set(add_result)
    return pt.Seq(
        app.state.result.set(add_result),
        output.set(add_result),
    )


@app.external(read_only=True)
def read_result(*, output: pt.abi.Uint64) -> pt.Expr:
    return output.set(app.state.result.get())


if __name__ == "__main__":
    spec = app.build()
    spec.export("artifacts")
