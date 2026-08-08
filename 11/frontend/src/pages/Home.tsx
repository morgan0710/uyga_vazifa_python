import { useState, useEffect, useRef } from 'react'
import { 
  GraduationCap, Users, Calendar, BookOpen, BarChart3, Settings, 
  ChevronRight, Search, Bell, Menu, X, TrendingUp, Clock, 
  UserPlus, FileText, Star, ArrowRight, Sparkles, Zap, 
  Target, Award, CalendarDays, CheckCircle2, AlertCircle,
  MoreVertical, Phone, Mail, ChevronDown, Filter
} from 'lucide-react'

// ========== MOUSE FOLLOWER COMPONENT ==========
function MouseFollower() {
  const [position, setPosition] = useState({ x: 0, y: 0 })
  const [isHovering, setIsHovering] = useState(false)

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      setPosition({ x: e.clientX, y: e.clientY })
    }
    const handleMouseOver = (e: MouseEvent) => {
      if ((e.target as HTMLElement).closest('button, a, .card-interactive, input')) {
        setIsHovering(true)
      } else {
        setIsHovering(false)
      }
    }
    window.addEventListener('mousemove', handleMouseMove)
    window.addEventListener('mouseover', handleMouseOver)
    return () => {
      window.removeEventListener('mousemove', handleMouseMove)
      window.removeEventListener('mouseover', handleMouseOver)
    }
  }, [])

  return (
    <div
      className="pointer-events-none fixed top-0 left-0 z-50 mix-blend-difference transition-transform duration-150 ease-out"
      style={{
        transform: `translate(${position.x - 20}px, ${position.y - 20}px) scale(${isHovering ? 2 : 1})`,
      }}
    >
      <div className="h-10 w-10 rounded-full bg-violet-500/30 blur-sm" />
    </div>
  )
}

// ========== ANIMATED BACKGROUND ==========
function AnimatedBackground() {
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 })
  
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      setMousePos({ x: e.clientX, y: e.clientY })
    }
    window.addEventListener('mousemove', handleMouseMove)
    return () => window.removeEventListener('mousemove', handleMouseMove)
  }, [])

  return (
    <div className="pointer-events-none fixed inset-0 z-0 overflow-hidden">
      <div
        className="absolute h-[600px] w-[600px] rounded-full opacity-20 blur-[120px] transition-all duration-1000 ease-out"
        style={{
          background: 'radial-gradient(circle, rgba(124,58,237,0.4) 0%, rgba(59,130,246,0.2) 50%, transparent 70%)',
          left: mousePos.x - 300,
          top: mousePos.y - 300,
        }}
      />
      <div
        className="absolute h-[400px] w-[400px] rounded-full opacity-10 blur-[100px] transition-all duration-[1500ms] ease-out"
        style={{
          background: 'radial-gradient(circle, rgba(236,72,153,0.3) 0%, rgba(168,85,247,0.2) 50%, transparent 70%)',
          left: mousePos.x - 200 + 200,
          top: mousePos.y - 200 + 150,
        }}
      />
    </div>
  )
}

// ========== FLOATING PARTICLES ==========
function FloatingParticles() {
  const particles = Array.from({ length: 20 }, (_, i) => ({
    id: i,
    size: Math.random() * 4 + 2,
    x: Math.random() * 100,
    y: Math.random() * 100,
    duration: Math.random() * 20 + 15,
    delay: Math.random() * 10,
    opacity: Math.random() * 0.3 + 0.1,
  }))

  return (
    <div className="pointer-events-none fixed inset-0 z-0 overflow-hidden">
      {particles.map((p) => (
        <div
          key={p.id}
          className="absolute rounded-full bg-violet-400"
          style={{
            width: p.size,
            height: p.size,
            left: `${p.x}%`,
            top: `${p.y}%`,
            opacity: p.opacity,
            animation: `float ${p.duration}s ${p.delay}s infinite ease-in-out`,
          }}
        />
      ))}
    </div>
  )
}

// ========== TILT CARD COMPONENT ==========
function TiltCard({ children, className = '' }: { children: React.ReactNode; className?: string }) {
  const ref = useRef<HTMLDivElement>(null)
  const [tilt, setTilt] = useState({ x: 0, y: 0 })
  const [isHovered, setIsHovered] = useState(false)

  const handleMouseMove = (e: React.MouseEvent) => {
    if (!ref.current) return
    const rect = ref.current.getBoundingClientRect()
    const x = (e.clientX - rect.left) / rect.width - 0.5
    const y = (e.clientY - rect.top) / rect.height - 0.5
    setTilt({ x: y * -10, y: x * 10 })
  }

  const handleMouseLeave = () => {
    setTilt({ x: 0, y: 0 })
    setIsHovered(false)
  }

  return (
    <div
      ref={ref}
      className={`card-interactive transition-all duration-300 ease-out ${className}`}
      style={{
        transform: `perspective(1000px) rotateX(${tilt.x}deg) rotateY(${tilt.y}deg) scale(${isHovered ? 1.02 : 1})`,
      }}
      onMouseMove={handleMouseMove}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={handleMouseLeave}
    >
      {children}
    </div>
  )
}

// ========== STAT CARD ==========
interface StatCardProps {
  icon: React.ReactNode
  title: string
  value: string
  change: string
  changeType: 'up' | 'down'
  color: string
}

function StatCard({ icon, title, value, change, changeType, color }: StatCardProps) {
  return (
    <TiltCard className="relative overflow-hidden rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur-xl">
      <div className={`absolute -top-4 -right-4 h-24 w-24 rounded-full opacity-10 blur-2xl ${color}`} />
      <div className="relative flex items-start justify-between">
        <div>
          <p className="text-sm font-medium text-slate-400">{title}</p>
          <p className="mt-2 text-3xl font-bold text-white">{value}</p>
          <div className={`mt-2 flex items-center gap-1 text-sm ${changeType === 'up' ? 'text-emerald-400' : 'text-red-400'}`}>
            <TrendingUp className="h-3 w-3" />
            <span>{change}</span>
          </div>
        </div>
        <div className={`rounded-xl p-3 ${color} bg-opacity-10`}>
          <div className={`text-white/80`}>{icon}</div>
        </div>
      </div>
    </TiltCard>
  )
}

// ========== SIDEBAR ==========
interface SidebarProps {
  isOpen: boolean
  onClose: () => void
  activeItem: string
  setActiveItem: (item: string) => void
}

function Sidebar({ isOpen, onClose, activeItem, setActiveItem }: SidebarProps) {
  const menuItems = [
    { id: 'dashboard', label: 'Boshqaruv paneli', icon: BarChart3 },
    { id: 'students', label: "O'quvchilar", icon: Users },
    { id: 'courses', label: 'Kurslar', icon: BookOpen },
    { id: 'schedule', label: 'Jadval', icon: Calendar },
    { id: 'payments', label: "To'lovlar", icon: FileText },
    { id: 'teachers', label: "O'qituvchilar", icon: Star },
    { id: 'reports', label: 'Hisobotlar', icon: TrendingUp },
    { id: 'settings', label: 'Sozlamalar', icon: Settings },
  ]

  return (
    <>
      {/* Mobile overlay */}
      {isOpen && (
        <div className="fixed inset-0 z-40 bg-black/50 backdrop-blur-sm lg:hidden" onClick={onClose} />
      )}
      
      <aside className={`fixed top-0 left-0 z-40 h-full w-72 border-r border-white/5 bg-slate-950/80 backdrop-blur-2xl transition-transform duration-300 lg:translate-x-0 ${isOpen ? 'translate-x-0' : '-translate-x-full'}`}>
        {/* Logo */}
        <div className="flex items-center gap-3 border-b border-white/5 p-6">
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-violet-500 to-blue-500">
            <GraduationCap className="h-6 w-6 text-white" />
          </div>
          <div>
            <h1 className="text-lg font-bold text-white">EduCRM</h1>
            <p className="text-xs text-slate-400">O'quv markazi</p>
          </div>
          <button onClick={onClose} className="ml-auto rounded-lg p-1 text-slate-400 hover:bg-white/5 lg:hidden">
            <X className="h-5 w-5" />
          </button>
        </div>

        {/* Navigation */}
        <nav className="space-y-1 p-4">
          {menuItems.map((item) => {
            const Icon = item.icon
            const isActive = activeItem === item.id
            return (
              <button
                key={item.id}
                onClick={() => {
                  setActiveItem(item.id)
                  onClose()
                }}
                className={`card-interactive group flex w-full items-center gap-3 rounded-xl px-4 py-3 text-sm font-medium transition-all duration-200 ${
                  isActive
                    ? 'bg-gradient-to-r from-violet-500/20 to-blue-500/10 text-white shadow-lg shadow-violet-500/10'
                    : 'text-slate-400 hover:bg-white/5 hover:text-white'
                }`}
              >
                <Icon className={`h-5 w-5 transition-colors ${isActive ? 'text-violet-400' : 'text-slate-500 group-hover:text-violet-400'}`} />
                <span>{item.label}</span>
                {isActive && <ChevronRight className="ml-auto h-4 w-4 text-violet-400" />}
              </button>
            )
          })}
        </nav>

        {/* Upgrade Card */}
        <div className="absolute bottom-6 left-4 right-4">
          <div className="card-interactive overflow-hidden rounded-2xl border border-violet-500/20 bg-gradient-to-br from-violet-500/10 to-blue-500/5 p-4">
            <Sparkles className="mb-2 h-8 w-8 text-violet-400" />
            <h3 className="text-sm font-semibold text-white">Premium versiya</h3>
            <p className="mt-1 text-xs text-slate-400">Barcha funksiyalarni oching</p>
            <button className="mt-3 flex w-full items-center justify-center gap-2 rounded-xl bg-gradient-to-r from-violet-500 to-blue-500 py-2 text-sm font-medium text-white transition-all hover:shadow-lg hover:shadow-violet-500/25">
              <Zap className="h-4 w-4" />
              Yangilash
            </button>
          </div>
        </div>
      </aside>
    </>
  )
}

// ========== HEADER ==========
function Header({ onMenuClick, onNotificationClick }: { onMenuClick: () => void; onNotificationClick: () => void }) {
  return (
    <header className="sticky top-0 z-30 border-b border-white/5 bg-slate-950/60 backdrop-blur-xl">
      <div className="flex h-16 items-center justify-between px-4 lg:px-8">
        <div className="flex items-center gap-4">
          <button onClick={onMenuClick} className="rounded-xl p-2 text-slate-400 hover:bg-white/5 lg:hidden">
            <Menu className="h-5 w-5" />
          </button>
          <div className="relative hidden sm:block">
            <Search className="absolute top-1/2 left-3 h-4 w-4 -translate-y-1/2 text-slate-500" />
            <input
              type="text"
              placeholder="Qidirish..."
              className="card-interactive w-72 rounded-xl border border-white/5 bg-white/5 py-2.5 pr-4 pl-10 text-sm text-white placeholder-slate-500 outline-none transition-all focus:border-violet-500/50 focus:bg-white/10 focus:ring-2 focus:ring-violet-500/20"
            />
          </div>
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={onNotificationClick}
            className="card-interactive relative rounded-xl p-2.5 text-slate-400 transition-all hover:bg-white/5 hover:text-white"
          >
            <Bell className="h-5 w-5" />
            <span className="absolute top-1.5 right-1.5 h-2 w-2 rounded-full bg-violet-500" />
          </button>

          <div className="card-interactive flex items-center gap-3 rounded-xl p-1.5 transition-all hover:bg-white/5">
            <div className="h-9 w-9 rounded-xl bg-gradient-to-br from-violet-500 to-blue-500 p-[1px]">
              <div className="flex h-full w-full items-center justify-center rounded-[10px] bg-slate-900">
                <span className="text-sm font-bold text-white">A</span>
              </div>
            </div>
            <div className="hidden text-left md:block">
              <p className="text-sm font-medium text-white">Admin</p>
              <p className="text-xs text-slate-400">Boshqaruvchi</p>
            </div>
            <ChevronDown className="hidden h-4 w-4 text-slate-400 md:block" />
          </div>
        </div>
      </div>
    </header>
  )
}

// ========== STUDENT ROW ==========
interface StudentProps {
  name: string
  course: string
  phone: string
  status: 'active' | 'inactive' | 'new'
  progress: number
  nextPayment: string
}

function StudentRow({ name, course, phone, status, progress, nextPayment }: StudentProps) {
  const statusConfig = {
    active: { label: 'Faol', color: 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20' },
    inactive: { label: 'Nofaol', color: 'bg-red-500/10 text-red-400 border-red-500/20' },
    new: { label: 'Yangi', color: 'bg-blue-500/10 text-blue-400 border-blue-500/20' },
  }

  return (
    <TiltCard className="group border-white/5 bg-white/[0.02]">
      <div className="p-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-4">
            <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-gradient-to-br from-violet-500/20 to-blue-500/10 text-white">
              <span className="text-sm font-bold">{name.split(' ').map(n => n[0]).join('')}</span>
            </div>
            <div>
              <p className="font-semibold text-white">{name}</p>
              <p className="text-xs text-slate-400">{course}</p>
            </div>
          </div>
          <div className="hidden items-center gap-4 md:flex">
            <div className="flex items-center gap-2 text-slate-400">
              <Phone className="h-3.5 w-3.5" />
              <span className="text-sm">{phone}</span>
            </div>
            <div className="w-24">
              <div className="h-1.5 overflow-hidden rounded-full bg-white/5">
                <div
                  className="h-full rounded-full bg-gradient-to-r from-violet-500 to-blue-500 transition-all duration-500"
                  style={{ width: `${progress}%` }}
                />
              </div>
              <p className="mt-1 text-right text-[10px] text-slate-500">{progress}%</p>
            </div>
            <span className={`rounded-lg border px-2.5 py-1 text-xs font-medium ${statusConfig[status].color}`}>
              {statusConfig[status].label}
            </span>
            <button className="rounded-lg p-1.5 text-slate-500 opacity-0 transition-all hover:bg-white/5 hover:text-white group-hover:opacity-100">
              <MoreVertical className="h-4 w-4" />
            </button>
          </div>
        </div>
        <div className="mt-3 flex items-center justify-between border-t border-white/5 pt-3 md:hidden">
          <div className="flex items-center gap-2 text-slate-400">
            <Phone className="h-3.5 w-3.5" />
            <span className="text-sm">{phone}</span>
          </div>
          <span className={`rounded-lg border px-2.5 py-1 text-xs font-medium ${statusConfig[status].color}`}>
            {statusConfig[status].label}
          </span>
        </div>
        <div className="mt-3 flex items-center justify-between border-t border-white/5 pt-3 md:hidden">
          <div className="w-full">
            <div className="flex items-center justify-between">
              <span className="text-xs text-slate-400">Progress</span>
              <span className="text-xs text-white">{progress}%</span>
            </div>
            <div className="mt-1 h-1.5 overflow-hidden rounded-full bg-white/5">
              <div
                className="h-full rounded-full bg-gradient-to-r from-violet-500 to-blue-500 transition-all duration-500"
                style={{ width: `${progress}%` }}
              />
            </div>
          </div>
        </div>
      </div>
    </TiltCard>
  )
}

// ========== SCHEDULE ITEM ==========
function ScheduleItem({ time, course, teacher, room, color }: { time: string; course: string; teacher: string; room: string; color: string }) {
  return (
    <TiltCard className="group border-white/5 bg-white/[0.02]">
      <div className="flex items-center gap-4 p-4">
        <div className={`flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-xl ${color}`}>
          <CalendarDays className="h-5 w-5 text-white" />
        </div>
        <div className="flex-1">
          <p className="font-medium text-white">{course}</p>
          <div className="flex items-center gap-3 text-xs text-slate-400">
            <span className="flex items-center gap-1">
              <Clock className="h-3 w-3" />
              {time}
            </span>
            <span className="flex items-center gap-1">
              <Users className="h-3 w-3" />
              {teacher}
            </span>
            <span>Xona: {room}</span>
          </div>
        </div>
        <button className="rounded-lg p-2 text-slate-500 opacity-0 transition-all hover:bg-white/5 hover:text-white group-hover:opacity-100">
          <ChevronRight className="h-4 w-4" />
        </button>
      </div>
    </TiltCard>
  )
}

// ========== ACTIVITY ITEM ==========
function ActivityItem({ icon, text, time, color }: { icon: React.ReactNode; text: string; time: string; color: string }) {
  return (
    <div className="flex items-start gap-3 py-3">
      <div className={`flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-lg ${color}`}>
        {icon}
      </div>
      <div className="flex-1">
        <p className="text-sm text-slate-300">{text}</p>
        <p className="text-xs text-slate-500">{time}</p>
      </div>
    </div>
  )
}

// ========== MAIN DASHBOARD ==========
export default function Home() {
  const [sidebarOpen, setSidebarOpen] = useState(false)
  const [activeItem, setActiveItem] = useState('dashboard')

  const stats = [
    { icon: <Users className="h-5 w-5" />, title: "Jami o'quvchilar", value: '1,248', change: "+12% o'sish", changeType: 'up' as const, color: 'bg-violet-500' },
    { icon: <BookOpen className="h-5 w-5" />, title: 'Faol kurslar', value: '24', change: "+3 yangi", changeType: 'up' as const, color: 'bg-blue-500' },
    { icon: <TrendingUp className="h-5 w-5" />, title: "Oylik daromad", value: '85.4M', change: "+18% o'sish", changeType: 'up' as const, color: 'bg-emerald-500' },
    { icon: <Target className="h-5 w-5" />, title: "Davomat", value: '94%', change: "+2% yaxshilandi", changeType: 'up' as const, color: 'bg-amber-500' },
  ]

  const students = [
    { name: 'Azizbek Karimov', course: 'Frontend Dasturlash', phone: '+998 90 123 45 67', status: 'active' as const, progress: 85, nextPayment: '15 Avg' },
    { name: 'Nodira Rashidova', course: 'UI/UX Dizayn', phone: '+998 91 234 56 78', status: 'active' as const, progress: 72, nextPayment: '20 Avg' },
    { name: 'Sardor Normatov', course: 'Backend Dasturlash', phone: '+998 93 345 67 89', status: 'new' as const, progress: 15, nextPayment: '25 Avg' },
    { name: 'Malika Toshmatova', course: 'Grafik Dizayn', phone: '+998 94 456 78 90', status: 'inactive' as const, progress: 60, nextPayment: 'Xech qachon' },
    { name: 'Jasurbek Alimov', course: 'Mobile Dasturlash', phone: '+998 97 567 89 01', status: 'active' as const, progress: 92, nextPayment: '10 Avg' },
  ]

  const schedule = [
    { time: '09:00 - 10:30', course: 'Frontend Asoslari', teacher: 'Sardor Umarov', room: '201', color: 'bg-gradient-to-br from-violet-500 to-purple-600' },
    { time: '11:00 - 12:30', course: 'UI/UX Dizayn', teacher: 'Nargiza Karimova', room: '305', color: 'bg-gradient-to-br from-blue-500 to-cyan-500' },
    { time: '14:00 - 15:30', course: 'Python Dasturlash', teacher: 'Otabek Mirzoev', room: '102', color: 'bg-gradient-to-br from-emerald-500 to-teal-500' },
    { time: '16:00 - 17:30', course: 'Grafik Dizayn', teacher: 'Dilshod Toshmatov', room: '401', color: 'bg-gradient-to-br from-amber-500 to-orange-500' },
  ]

  const activities = [
    { icon: <UserPlus className="h-4 w-4 text-emerald-400" />, text: "Yangi o'quvchi qo'shildi: Sardor Normatov", time: "5 daqiqa oldin", color: 'bg-emerald-500/10' },
    { icon: <CheckCircle2 className="h-4 w-4 text-blue-400" />, text: "To'lov qabul qilindi: Azizbek Karimov - 1,200,000 so'm", time: "15 daqiqa oldin", color: 'bg-blue-500/10' },
    { icon: <AlertCircle className="h-4 w-4 text-amber-400" />, text: "To'lov muddati o'tgan: Malika Toshmatova", time: "1 soat oldin", color: 'bg-amber-500/10' },
    { icon: <Award className="h-4 w-4 text-violet-400" />, text: "Sertifikat berildi: Jasurbek Alimov", time: "2 soat oldin", color: 'bg-violet-500/10' },
  ]

  return (
    <div className="min-h-screen bg-[#0a0a1a] text-white">
      <MouseFollower />
      <AnimatedBackground />
      <FloatingParticles />

      <div className="relative flex">
        <Sidebar isOpen={sidebarOpen} onClose={() => setSidebarOpen(false)} activeItem={activeItem} setActiveItem={setActiveItem} />

        <main className="flex-1 lg:ml-72">
          <Header onMenuClick={() => setSidebarOpen(true)} onNotificationClick={() => {}} />

          <div className="p-4 lg:p-8">
            {/* Welcome Section */}
            <div className="mb-8">
              <h2 className="text-2xl font-bold text-white lg:text-3xl">
                Xush kelibsiz! 👋
              </h2>
              <p className="mt-1 text-slate-400">Bugungi holat va yangiliklar</p>
            </div>

            {/* Stats Grid */}
            <div className="mb-8 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
              {stats.map((stat, i) => (
                <StatCard key={i} {...stat} />
              ))}
            </div>

            {/* Main Content Grid */}
            <div className="grid grid-cols-1 gap-6 xl:grid-cols-3">
              {/* Students Table */}
              <div className="xl:col-span-2">
                <TiltCard className="border-white/5 bg-white/[0.02]">
                  <div className="flex items-center justify-between border-b border-white/5 p-5">
                    <div>
                      <h3 className="text-lg font-semibold text-white">O'quvchilar ro'yxati</h3>
                      <p className="text-sm text-slate-400">Jami 1,248 ta o'quvchi</p>
                    </div>
                    <div className="flex items-center gap-2">
                      <button className="card-interactive flex items-center gap-2 rounded-xl border border-white/10 px-4 py-2 text-sm text-slate-400 transition-all hover:border-violet-500/50 hover:text-white">
                        <Filter className="h-4 w-4" />
                        <span className="hidden sm:inline">Filtrlash</span>
                      </button>
                      <button className="card-interactive flex items-center gap-2 rounded-xl bg-gradient-to-r from-violet-500 to-blue-500 px-4 py-2 text-sm font-medium text-white transition-all hover:shadow-lg hover:shadow-violet-500/25">
                        <UserPlus className="h-4 w-4" />
                        <span className="hidden sm:inline">Qo'shish</span>
                      </button>
                    </div>
                  </div>
                  <div className="divide-y divide-white/5">
                    {students.map((student, i) => (
                      <StudentRow key={i} {...student} />
                    ))}
                  </div>
                  <div className="border-t border-white/5 p-4">
                    <button className="card-interactive flex w-full items-center justify-center gap-2 rounded-xl py-2.5 text-sm font-medium text-violet-400 transition-all hover:bg-white/5">
                      Barcha o'quvchilarni ko'rish
                      <ArrowRight className="h-4 w-4" />
                    </button>
                  </div>
                </TiltCard>
              </div>

              {/* Right Sidebar */}
              <div className="space-y-6">
                {/* Today's Schedule */}
                <TiltCard className="border-white/5 bg-white/[0.02]">
                  <div className="flex items-center justify-between border-b border-white/5 p-5">
                    <div>
                      <h3 className="text-lg font-semibold text-white">Bugungi darslar</h3>
                      <p className="text-sm text-slate-400">4 ta dars rejalashtirilgan</p>
                    </div>
                    <Calendar className="h-5 w-5 text-slate-400" />
                  </div>
                  <div className="divide-y divide-white/5">
                    {schedule.map((item, i) => (
                      <ScheduleItem key={i} {...item} />
                    ))}
                  </div>
                </TiltCard>

                {/* Recent Activity */}
                <TiltCard className="border-white/5 bg-white/[0.02]">
                  <div className="flex items-center justify-between border-b border-white/5 p-5">
                    <div>
                      <h3 className="text-lg font-semibold text-white">So'nggi yangiliklar</h3>
                      <p className="text-sm text-slate-400">Bugungi faoliyat</p>
                    </div>
                    <Bell className="h-5 w-5 text-slate-400" />
                  </div>
                  <div className="divide-y divide-white/5 px-5">
                    {activities.map((activity, i) => (
                      <ActivityItem key={i} {...activity} />
                    ))}
                  </div>
                </TiltCard>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  )
}
