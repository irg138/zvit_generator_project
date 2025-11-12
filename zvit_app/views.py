import io
import zipfile
from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
from datetime import datetime
from .forms import ZvitForm
from . import utils

BASE_DIR = Path(__file__).resolve().parent.parent


def index(request):
    if request.method == "POST":
        form = ZvitForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # === Формирование групп ===
            group_zvit = "\n".join(
                [("\t" * 7 + name if i > 0 else name)
                 for i, name in enumerate(data.get("zvit_members", []))]
            ) if data.get("zvit_members") else ""

            group_rozp = "\n".join(data.get("rozp_members", [])) if data.get("rozp_members") else ""

            # === Замены для шаблонов ===
            replacements = {
                "№ЗАЯВКИ": data.get("num") or "",
                "ДАТА_ЗАЯВКИ": data.get("date") or "",
                "ОБЄКТ": data.get("object") or "",
                "СФЕРА": utils.SPHERES.get(data.get("sphere"), data.get("sphere") or ""),
                "ГрупаЗвіт": group_zvit,
                "ГрупаВсеРозпорядження": group_rozp,
                "ВІДПОВІДАЛЬНИЙ": data.get("responsible") or "",
                "КЕРІВНИК": data.get("leader") or "",
                "КЕРІВНИК_OI": data.get("leader_oi") or "",
                "ДАТА_РОЗПОРЯДЖЕННЯ": data.get("date_rozp") or "",
            }

            # === Имя архива по полю id_object ===
            id_object = data.get("id_object") or data.get("object") or "Без_назви"
            safe_name = utils.sanitize_filename(str(id_object)) or "Без_назви"

            # === Пути к шаблонам ===
            template_zvit = BASE_DIR / "Звіт.docx"
            template_rozp = BASE_DIR / "Розпорядження.docx"

            # === Генерация файлов в памяти ===
            in_mem = io.BytesIO()
            with zipfile.ZipFile(in_mem, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
                # временные имена внутри архива
                out_name_zvit = f"Звіт_{safe_name}.docx"
                out_name_rozp = f"Розпорядження_{safe_name}.docx"

                # временные файлы на диске
                tmp_zvit = BASE_DIR / f"__tmp_{out_name_zvit}"
                tmp_rozp = BASE_DIR / f"__tmp_{out_name_rozp}"

                # === Замена плейсхолдеров ===
                utils.replace_placeholders(str(template_zvit), replacements, str(tmp_zvit))
                utils.replace_placeholders(str(template_rozp), replacements, str(tmp_rozp))

                # === Добавление файлов в архив ===
                zf.write(tmp_zvit, arcname=out_name_zvit)
                zf.write(tmp_rozp, arcname=out_name_rozp)

                # === Очистка временных файлов ===
                for tmp_file in (tmp_zvit, tmp_rozp):
                    try:
                        tmp_file.unlink(missing_ok=True)
                    except Exception:
                        pass

            # === Формирование ответа ===
            in_mem.seek(0)
            zip_name = f"{safe_name}.zip"
            response = HttpResponse(in_mem.read(), content_type="application/zip")
            # корректно обрабатывает кириллицу и спецсимволы
            response["Content-Disposition"] = f"attachment; filename*=UTF-8''{zip_name}"
            return response

    # === GET-запрос ===
    else:
        form = ZvitForm()

    return render(request, "zvit_app/form.html", {"form": form})
