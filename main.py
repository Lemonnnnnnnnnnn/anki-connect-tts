import argparse
from anki_utils import get_empty_audio_cards, get_note_by_timestamp, get_card_fields, store_audio_to_anki, \
    update_card_audio
from tts_utils import infer_audio


def add_audio_to_all_notes():
    note_ids = get_empty_audio_cards()
    if not note_ids:
        print("没有需要处理的卡片")
        return

    notes = get_card_fields(note_ids)
    texts = [note['fields']['Context']['value'] for note in notes]

    # for text in texts:
    #     wavs = infer_audio([text])

    for i, note in enumerate(notes):
        wavs = infer_audio([texts[i]])
        note_id = note['noteId']
        wav_data = wavs[0]

        audio_filename = store_audio_to_anki(wav_data, note_id)
        update_card_audio(note_id, audio_filename)
        print(f"为卡片 {note_id} 添加了音频")


def update_audio_for_notes(timestamp):
    note_ids = get_note_by_timestamp(timestamp)
    if not note_ids:
        print("没有找到符合时间戳的卡片")
        return

    notes = get_card_fields(note_ids)
    texts = [note['fields']['Context']['value'] for note in notes]

    wavs = infer_audio(texts)

    for i, note in enumerate(notes):
        note_id = note['noteId']
        wav_data = wavs[i]

        audio_filename = store_audio_to_anki(wav_data, note_id)
        update_card_audio(note_id, audio_filename)
        print(f"为卡片 {note_id} 添加了音频")


def main():
    parser = argparse.ArgumentParser(description="Anki Audio Manager")
    parser.add_argument('--add', action='store_true', help='Add audio to all notes with missing audio')
    parser.add_argument('--update', type=str, help='Update audio for notes with a specific timestamp')

    args = parser.parse_args()

    if args.add:
        add_audio_to_all_notes()
    elif args.update:
        if not args.update:
            print("请提供时间戳")
        else:
            update_audio_for_notes(args.update)


if __name__ == "__main__":
    main()
