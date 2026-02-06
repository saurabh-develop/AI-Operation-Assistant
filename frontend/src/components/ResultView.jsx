export default function ResultView({ result }) {
  return <pre>{JSON.stringify(result, null, 2)}</pre>;
}
