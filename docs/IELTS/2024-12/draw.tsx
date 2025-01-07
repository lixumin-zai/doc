import { Tldraw } from 'tldraw'
import 'tldraw/tldraw.css'


export default function draw() {
	return (
		<div style={{ width: '800px', height: '600px', margin: '0 auto', border: '2px solid black'}}>
			<Tldraw />
		</div>
	)
}