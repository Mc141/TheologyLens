


function VerseCard({ verse }) {
  return (
    <div>
      <h3 className="verse-title">{verse.Reference}</h3>
      <p>{verse.Text}</p>
    </div>
  );
}

export default VerseCard;
