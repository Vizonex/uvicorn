def auto_loop_setup(use_subprocess: bool = False) -> None:
    try:
        import uvloop  # noqa
    except ImportError:  # pragma: no cover
        try:
            import winloop  # noqa
        except ImportError:
            from uvicorn.loops.asyncio import asyncio_setup as loop_setup

            loop_setup(use_subprocess=use_subprocess)
        else:
            from uvicorn.loops.winloop import winloop_setup as loop_setup

            loop_setup(use_subprocess=use_subprocess)
    else:  # pragma: no cover
        from uvicorn.loops.uvloop import uvloop_setup
        uvloop_setup(use_subprocess=use_subprocess)

