from pathlib import Path
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

import flet as ft
import flet.testing as ftt
import pytest
import pytest_asyncio
import examples.cupertino_action_sheet as cas


@pytest_asyncio.fixture(scope="module")
async def flet_app(request):
    flet_app = ftt.FletTestApp(
        flutter_app_dir=(Path(__file__).parent / "../../../../../../client").resolve(),
        flet_app_main=cas.main,
        test_path=request.fspath,
    )
    await flet_app.start()
    yield flet_app
    await flet_app.teardown()


@pytest.mark.asyncio(loop_scope="module")
async def test_cas(flet_app: ftt.FletTestApp):
    tester = flet_app.tester
    await tester.pump_and_settle()
    open_text = await tester.find_by_text("Open CupertinoBottomSheet")
    assert open_text.count == 1
    await tester.tap(open_text)

    # tap open dialog
    # dialog_btn = await tester.find_by_key(123)
    # assert dialog_btn.count == 1
    # await tester.tap(dialog_btn)
    # await tester.pump_and_settle()
    # action_sheet = await tester.find_by_key(456)
    # assert action_sheet.count == 1
