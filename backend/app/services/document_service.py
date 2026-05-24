from pathlib import Path
import fitz
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "data" / "uploads"

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


class DocumentService:

    def save_file(
        self,
        file_name: str,
        content: bytes
    ) -> str:

        file_path = UPLOAD_DIR / file_name

        with open(file_path, "wb") as f:
            f.write(content)

        return str(file_path)

    def extract_text(
        self,
        file_path: str
    ) -> str:

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return self._extract_pdf(
                file_path
            )

        elif extension == ".txt":
            return self._extract_txt(
                file_path
            )

        elif extension == ".csv":
            return self._extract_csv(
                file_path
            )

        raise ValueError(
            "Unsupported file type"
        )

    def _extract_pdf(
        self,
        file_path: str
    ) -> str:

        text = ""

        pdf = fitz.open(file_path)

        for page in pdf:
            text += page.get_text()

        pdf.close()

        return text

    def _extract_txt(
        self,
        file_path: str
    ) -> str:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()

    def _extract_csv(
        self,
        file_path: str
    ) -> str:

        df = pd.read_csv(file_path)

        return df.to_string()


document_service = DocumentService()