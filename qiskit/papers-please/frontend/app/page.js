import styles from './home.module.css';
import icon from '../public/icon.svg';
import Image from 'next/image';

export default function Home() {
	return (
		<main className={styles.page}>
			<div className={styles.card}>
				<header>
					<Image
						src={icon}
						background='#100e0c'
						alt='papers please icon'
					/>
				</header>

				<section className={styles.inputsContainer}>
					<h1 className={styles.inputsTitle}>Input Data</h1>
					<ul className={styles.inputs}>
						<li className={styles.input}>
							<label for='bribe' className={styles.inputText}>
								Bribe
							</label>
							<input type='checkbox' name='bribe' />
						</li>
						<li className={styles.input}>
							<label
								for='false_info'
								className={styles.inputText}
							>
								False Info
							</label>
							<input type='checkbox' name='false_info' />
						</li>
						<li className={styles.input}>
							<label for='wanted' className={styles.inputText}>
								Wanted
							</label>
							<input type='checkbox' name='wanted' />
						</li>
						<li className={styles.input}>
							<label for='passport' className={styles.inputText}>
								Passport
							</label>
							<input type='checkbox' name='passport' />
						</li>
						<li className={styles.input}>
							<label for='documents' className={styles.inputText}>
								Documents
							</label>
							<input type='checkbox' name='documents' />
						</li>
					</ul>
				</section>
			</div>
		</main>
	);
}
